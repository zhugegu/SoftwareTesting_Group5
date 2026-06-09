"""Member C marshal stability tests.

This script tests marshal stability and correctness for container types,
set/frozenset non-determinism, and large container memory boundaries.
It covers requirements: R4.1, R4.2, R4.3, R4.4, R4.5.
"""

import os
import sys
import marshal
import hashlib
import unittest
import subprocess


def get_marshal_hash(obj):
    serialized_bytes = marshal.dumps(obj)
    return hashlib.sha256(serialized_bytes).hexdigest()


if len(sys.argv) > 1 and sys.argv[1] == "--worker":
    TARGET_TYPE = sys.argv[2]
    if TARGET_TYPE == "set":
        print(get_marshal_hash({"apple", "banana", "cherry"}))
    elif TARGET_TYPE == "frozenset":
        print(get_marshal_hash(frozenset({"apple", "banana", "cherry"})))
    elif TARGET_TYPE == "nested":
        print(get_marshal_hash(["alpha", {"apple", "banana"}, ["beta", "gamma"]]))
    sys.exit(0)


class TestMarshalContainers(unittest.TestCase):

    def run_worker_multiple_times(self, target, env_seed=None):
        collected_hashes = set()
        current_env = os.environ.copy()
        if env_seed is not None:
            current_env["PYTHONHASHSEED"] = str(env_seed)
        else:
            current_env["PYTHONHASHSEED"] = "random"
        for _ in range(10):
            cmd = [sys.executable, __file__, "--worker", target]
            result = subprocess.run(
                cmd, env=current_env, capture_output=True, text=True, check=True
            )
            collected_hashes.add(result.stdout.strip())
        return collected_hashes

    # TC-C-01: Empty container determinism test
    def test_tc_c_01_empty_containers(self):
        hash_list = get_marshal_hash([])
        hash_dict = get_marshal_hash({})
        hash_set = get_marshal_hash(set())
        hash_tuple = get_marshal_hash(())
        self.assertEqual(hash_list, get_marshal_hash([]))
        self.assertEqual(hash_dict, get_marshal_hash({}))
        self.assertEqual(hash_set, get_marshal_hash(set()))
        self.assertEqual(hash_tuple, get_marshal_hash(()))
        print("\n[TC-C-01] Empty containers: Serialized twice, hashes identical -> Deterministic.")

    # TC-C-02: Ordered container consistency across multiple runs
    def test_tc_c_02_ordered_containers(self):
        lst = ["apple", "banana", "cherry"]
        dct = {"a": 1, "b": 2}
        self.assertEqual(get_marshal_hash(lst), get_marshal_hash(["apple", "banana", "cherry"]))
        self.assertEqual(get_marshal_hash(dct), get_marshal_hash({"a": 1, "b": 2}))
        print("[TC-C-02] Ordered containers (list/dict): Same content produces identical hashes -> Deterministic.")

    # TC-C-03: Set non-determinism under random seed
    def test_tc_c_03_set_random_seed(self):
        collected_hashes = self.run_worker_multiple_times("set", env_seed=None)
        print(f"[TC-C-03 Observation] Under random seed, string set produced {len(collected_hashes)} different hashes in 10 runs.")
        self.assertTrue(
            len(collected_hashes) > 1,
            "Bug: marshal didn't capture random seed changes, set order is always the same!"
        )
        print("[TC-C-03 Conclusion] Set type is indeed non-deterministic due to PYTHONHASHSEED.")

    # TC-C-04: Frozenset non-determinism under random seed
    def test_tc_c_04_frozenset_random_seed(self):
        collected_hashes = self.run_worker_multiple_times("frozenset", env_seed=None)
        print(f"[TC-C-04 Observation] Under random seed, frozenset produced {len(collected_hashes)} different hashes in 10 runs.")
        self.assertTrue(len(collected_hashes) > 1, "Bug: frozenset doesn't exhibit non-determinism!")
        print("[TC-C-04 Conclusion] Immutable sets (frozenset) are also affected by hash randomization and are non-deterministic.")

    # TC-C-05: Set determinism restoration with fixed seed
    def test_tc_c_05_set_fixed_seed(self):
        collected_hashes = self.run_worker_multiple_times("set", env_seed=123)
        print(f"[TC-C-05 Observation] With fixed seed (123), set produced {len(collected_hashes)} different hashes in 10 runs.")
        self.assertEqual(len(collected_hashes), 1, "Bug: Set serialization still changes after fixing seed!")
        print("[TC-C-05 Conclusion] Fixing PYTHONHASHSEED restores determinism to set serialization.")

    # TC-C-06: Large container memory boundary and stability test
    def test_tc_c_06_large_containers(self):
        try:
            large_list = list(range(10**6))
            large_dict = dict.fromkeys(range(10**5), 0)
            self.assertEqual(get_marshal_hash(large_list), get_marshal_hash(large_list))
            self.assertEqual(get_marshal_hash(large_dict), get_marshal_hash(large_dict))
        except MemoryError:
            self.fail("Crash bug: marshal encountered memory overflow with million-scale containers!")
        except Exception as e:
            self.fail(f"Crash bug: Unexpected crash in large container test: {str(e)}")
        print("[TC-C-06] Large containers (1M list / 100K dict): No memory crash, serialization consistent -> Stability and determinism passed.")

    # TC-C-07: Non-determinism propagation in nested containers
    def test_tc_c_07_nested_propagation(self):
        collected_hashes = self.run_worker_multiple_times("nested", env_seed=None)
        print(f"[TC-C-07 Observation] Under random seed, nested list with set produced {len(collected_hashes)} different hashes in 10 runs.")
        self.assertTrue(len(collected_hashes) > 1, "Bug: Inner set randomness didn't propagate to outer list!")
        print("[TC-C-07 Conclusion] Non-determinism propagates from inner unordered containers to outer ordered containers.")

if __name__ == "__main__":
    unittest.main()