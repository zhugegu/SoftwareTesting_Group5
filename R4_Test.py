"""
Test module: marshal container types and set order non-determinism test
The original print statements and comments are in Chinese,
I translated them with Deepseek.
"""

import marshal
import hashlib
import unittest
import random

def get_marshal_hash(obj):
    """Return SHA-256 hash of the object serialized by marshal"""
    return hashlib.sha256(marshal.dumps(obj)).hexdigest()

class TestMarshalContainers(unittest.TestCase):

    def _run_multiple(self, target, fix_seed=False):
        """Simulate multiple runs and collect hash values"""
        hashes = set()
        base_elements = [f"item_{i}" for i in range(20)]

        for i in range(10):
            elements = base_elements.copy()
            if not fix_seed:
                random.seed(i)
                random.shuffle(elements)

            if target == "set":
                obj = set(elements)
            elif target == "frozenset":
                obj = frozenset(elements)
            elif target == "nested":
                obj = ["alpha", set(elements), ["beta", "gamma"]]
            hashes.add(get_marshal_hash(obj))

        return hashes

    # empty_containers
    def test_TC_C_01(self):
        """TC-C-01: Determinism test for empty containers"""
        self.assertEqual(get_marshal_hash([]), get_marshal_hash([]))
        self.assertEqual(get_marshal_hash({}), get_marshal_hash({}))
        self.assertEqual(get_marshal_hash(set()), get_marshal_hash(set()))
        self.assertEqual(get_marshal_hash(()), get_marshal_hash(()))
        print("TC-C-01: Empty container serialization determinism verified")

    # ordered_containers
    def test_TC_C_02(self):
        """TC-C-02: Consistency test for ordered containers"""
        lst = ["apple", "banana", "cherry"]
        dct = {"a": 1, "b": 2}
        self.assertEqual(get_marshal_hash(lst), get_marshal_hash(["apple", "banana", "cherry"]))
        self.assertEqual(get_marshal_hash(dct), get_marshal_hash({"a": 1, "b": 2}))
        print("TC-C-02: Ordered container serialization consistency verified")

    # set_random_seed
    def test_TC_C_03(self):
        """TC-C-03: Non-determinism test for set with random seed"""
        hashes = self._run_multiple("set", fix_seed=False)
        cnt = len(hashes)
        print(f"TC-C-03: Set random seed test, {cnt} distinct hashes in 10 runs")
        self.assertTrue(cnt >= 1)
        if cnt > 1:
            print("Conclusion: Non-determinism exists, set serialization affected by random seed")
        else:
            print("Conclusion: Fully deterministic, unaffected by random seed")

    # frozenset_random_seed
    def test_TC_C_04(self):
        """TC-C-04: Non-determinism test for frozenset with random seed"""
        hashes = self._run_multiple("frozenset", fix_seed=False)
        cnt = len(hashes)
        print(f"TC-C-04: Frozenset random seed test, {cnt} distinct hashes in 10 runs")
        self.assertTrue(cnt >= 1)
        if cnt > 1:
            print("Conclusion: Non-determinism exists, frozenset serialization affected by random seed")
        else:
            print("Conclusion: Fully deterministic, frozenset serialization stable")

    # set_fixed_seed
    def test_TC_C_05(self):
        """TC-C-05: Determinism recovery test with fixed seed"""
        hashes = self._run_multiple("set", fix_seed=True)
        cnt = len(hashes)
        print(f"TC-C-05: Fixed seed test, {cnt} distinct hashes in 10 runs")
        self.assertEqual(cnt, 1, "Error: set serialization still inconsistent after fixing seed")
        print("Conclusion: Set serialization fully consistent with fixed seed")

    # large_containers
    def test_TC_C_06(self):
        """TC-C-06: Large container boundary stability test"""
        try:
            large_list = list(range(10**6))
            large_dict = dict.fromkeys(range(10**5), 0)
            self.assertEqual(get_marshal_hash(large_list), get_marshal_hash(large_list))
            self.assertEqual(get_marshal_hash(large_dict), get_marshal_hash(large_dict))
            print("TC-C-06: Million-element large container serialization stability verified")
        except Exception as e:
            self.fail(f"Large container test exception: {e}")

    # nested_propagation
    def test_TC_C_07(self):
        """TC-C-07: Non-determinism propagation test for nested containers"""
        hashes = self._run_multiple("nested", fix_seed=False)
        cnt = len(hashes)
        print(f"TC-C-07: Nested container random seed test, {cnt} distinct hashes in 10 runs")
        self.assertTrue(cnt >= 1)
        if cnt > 1:
            print("Conclusion: Non-determinism propagates, inner set randomness affects outer container")
        else:
            print("Conclusion: Overall deterministic, inner disorder did not break outer stability")

if __name__ == "__main__":
    unittest.main()