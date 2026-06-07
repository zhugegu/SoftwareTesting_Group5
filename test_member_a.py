import marshal
import hashlib
import unittest
import sys
import os
import io


def hash_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def test_determinism(runs: int = 10):
    def decorator(func):
        def wrapper(*args, **kwargs):
            results = set()
            for _ in range(runs):
                result = func(*args, **kwargs)
                results.add(hash_bytes(result))
            assert len(results) == 1, (
                f"Non-deterministic behavior: {len(results)} different outputs "
                f"({func.__name__})"
            )
            return result
        return wrapper
    return decorator


class HelperMixin:
    def helper(self, sample, *extra):
        new = marshal.loads(marshal.dumps(sample, *extra))
        self.assertEqual(sample, new)
        
        try:
            with open("marshal_test.tmp", "wb") as f:
                marshal.dump(sample, f, *extra)
            with open("marshal_test.tmp", "rb") as f:
                new = marshal.load(f)
            self.assertEqual(sample, new)
        finally:
            if os.path.exists("marshal_test.tmp"):
                os.remove("marshal_test.tmp")
    
    def helper_bytesio(self, sample, *extra):
        bio = io.BytesIO()
        marshal.dump(sample, bio, *extra)
        bio.seek(0)
        new = marshal.load(bio)
        self.assertEqual(sample, new)


class TestR1_1_CoreDeterminism(unittest.TestCase, HelperMixin):
    @test_determinism()
    def test_none(self):
        return marshal.dumps(None)

    @test_determinism()
    def test_bool_true(self):
        return marshal.dumps(True)

    @test_determinism()
    def test_bool_false(self):
        return marshal.dumps(False)

    @test_determinism()
    def test_zero(self):
        return marshal.dumps(0)

    @test_determinism()
    def test_small_positive_int(self):
        return marshal.dumps(42)

    @test_determinism()
    def test_small_negative_int(self):
        return marshal.dumps(-42)

    @test_determinism()
    def test_empty_string(self):
        return marshal.dumps("")

    @test_determinism()
    def test_ascii_string(self):
        return marshal.dumps("hello world")

    @test_determinism()
    def test_unicode_string(self):
        return marshal.dumps("你好世界")

    @test_determinism()
    def test_empty_bytes(self):
        return marshal.dumps(b"")

    @test_determinism()
    def test_bytes(self):
        return marshal.dumps(b"hello world")

    def test_roundtrip_none(self):
        self.helper(None)

    def test_roundtrip_bool(self):
        for b in (True, False):
            self.helper(b)

    def test_roundtrip_small_ints(self):
        for i in range(-10, 11):
            self.helper(i)


class TestR2_1_CrossPlatformWordLength(unittest.TestCase, HelperMixin):
    @test_determinism()
    def test_int32_boundary_positive(self):
        return marshal.dumps(2**31 - 1)

    @test_determinism()
    def test_int32_boundary_negative(self):
        return marshal.dumps(-2**31)

    @test_determinism()
    def test_int32_overflow_positive(self):
        return marshal.dumps(2**31)

    @test_determinism()
    def test_int32_overflow_negative(self):
        return marshal.dumps(-2**31 - 1)

    @test_determinism()
    def test_int64_boundary_positive(self):
        return marshal.dumps(2**63 - 1)

    @test_determinism()
    def test_int64_boundary_negative(self):
        return marshal.dumps(-2**63)

    @test_determinism()
    def test_int64_overflow_positive(self):
        return marshal.dumps(2**63)

    @test_determinism()
    def test_int64_overflow_negative(self):
        return marshal.dumps(-2**63 - 1)

    @test_determinism()
    def test_large_integer_1000_bits(self):
        return marshal.dumps(2**1000)

    @test_determinism()
    def test_large_integer_10000_bits(self):
        return marshal.dumps(2**10000)

    @test_determinism()
    def test_negative_large_integer(self):
        return marshal.dumps(-2**1000)

    def test_wide_range_ints(self):
        n = sys.maxsize ** 2
        while n:
            for expected in (-n, n):
                self.helper(expected)
            n = n >> 1
        
        n = 1 << 100
        while n:
            for expected in (-n, -n+1, n-1, n):
                self.helper(expected)
            n = n >> 1

    def test_int64_direct(self):
        maxint64 = (1 << 63) - 1
        minint64 = -maxint64 - 1
        
        for base in maxint64, minint64, -maxint64, -(minint64 >> 1):
            while base:
                s = b'I' + int.to_bytes(base, 8, 'little', signed=True)
                got = marshal.loads(s)
                self.assertEqual(base, got)
                if base == -1:
                    base = 0
                else:
                    base >>= 1

        got = marshal.loads(b'I\xfe\xdc\xba\x98\x76\x54\x32\x10')
        self.assertEqual(got, 0x1032547698badcfe)
        got = marshal.loads(b'I\x01\x23\x45\x67\x89\xab\xcd\xef')
        self.assertEqual(got, -0x1032547698badcff)


class TestR2_2_VariableLengthEncodingBoundary(unittest.TestCase, HelperMixin):
    @test_determinism()
    def test_single_byte_int(self):
        results = []
        for i in range(256):
            results.append(marshal.dumps(i))
        return b''.join(results)

    @test_determinism()
    def test_two_byte_boundary(self):
        return marshal.dumps(0xFFFF)

    @test_determinism()
    def test_three_byte_boundary(self):
        return marshal.dumps(0xFFFFFF)

    @test_determinism()
    def test_four_byte_boundary(self):
        return marshal.dumps(0xFFFFFFFF)

    @test_determinism()
    def test_short_ascii_boundary(self):
        return marshal.dumps("a" * 255)

    @test_determinism()
    def test_short_ascii_boundary_plus_1(self):
        return marshal.dumps("a" * 256)

    @test_determinism()
    def test_negative_one(self):
        return marshal.dumps(-1)

    @test_determinism()
    def test_small_int_cache_boundary_positive(self):
        return marshal.dumps(257)

    @test_determinism()
    def test_small_int_cache_boundary_negative(self):
        return marshal.dumps(-257)

    @test_determinism()
    def test_marshal_long_digit_boundaries(self):
        boundaries = [32767, 32768, 1073741823, 1073741824]
        for val in boundaries:
            marshal.dumps(val)
            marshal.dumps(-val)
        return marshal.dumps(boundaries)

    def test_large_string(self):
        self.helper(" " * 10000)

    def test_file_stream_determinism(self):
        bio = io.BytesIO()
        marshal.dump(42, bio)
        stream_data = bio.getvalue()
        self.assertEqual(stream_data, marshal.dumps(42))


class TestR2_3_InternalOptimizationIsolation(unittest.TestCase, HelperMixin):
    @test_determinism()
    def test_interned_string(self):
        s = sys.intern("test_interned_string")
        return marshal.dumps(s)

    @test_determinism()
    def test_non_interned_string(self):
        s = "test_non_interned_string"
        return marshal.dumps(s)

    @test_determinism()
    def test_interned_vs_non_interned_same_content(self):
        interned = sys.intern("hello")
        non_interned = "hello"
        return marshal.dumps((interned, non_interned))

    @test_determinism()
    def test_small_int_cache(self):
        a = 42
        b = 42
        return marshal.dumps((a, b))

    @test_determinism()
    def test_large_int_no_cache(self):
        a = 1000
        b = 1000
        return marshal.dumps((a, b))

    @test_determinism()
    def test_repeated_interned_calls(self):
        results = []
        for _ in range(10):
            s = sys.intern("repeated_test")
            results.append(marshal.dumps(s))
        return b''.join(results)

    def test_intern_preservation(self):
        strobj = "this is an interned string"
        strobj = sys.intern(strobj)
        
        s = marshal.loads(marshal.dumps(strobj))
        self.assertEqual(s, strobj)
        self.assertEqual(id(s), id(strobj))
        
        s2 = marshal.loads(marshal.dumps(strobj, 2))
        self.assertEqual(s2, strobj)
        self.assertNotEqual(id(s2), id(strobj))

    def test_interned_vs_non_interned_string(self):
        s1 = "hello_world_test_strat"
        s2 = sys.intern("".join(["hello_", "world_", "test_", "strat"]))
        self.assertEqual(hash_bytes(marshal.dumps(s1)), hash_bytes(marshal.dumps(s2)))

    def test_small_int_pool_isolation(self):
        a = 256
        b = int("256")
        self.assertEqual(hash_bytes(marshal.dumps(a)), hash_bytes(marshal.dumps(b)))


class TestEdgeCases(unittest.TestCase, HelperMixin):
    @test_determinism()
    def test_one(self):
        return marshal.dumps(1)

    @test_determinism()
    def test_minus_one(self):
        return marshal.dumps(-1)

    @test_determinism()
    def test_bytes_with_zero(self):
        return marshal.dumps(b"\x00\x01\x02\xFF")

    @test_determinism()
    def test_mixed_string(self):
        return marshal.dumps("Hello 世界 123!@#")

    @test_determinism()
    def test_special_characters(self):
        return marshal.dumps("\n\t\r\b\f")


class TestDeterminismVerification(unittest.TestCase):
    def test_consistent_hash_output(self):
        test_cases = [
            None, True, False, 0, 42, -42,
            2**31 - 1, -2**31, 2**1000,
            "", "hello", "你好",
            b"", b"hello",
        ]
        
        for obj in test_cases:
            hashes = set()
            for _ in range(100):
                result = marshal.dumps(obj)
                hashes.add(hash_bytes(result))
            self.assertEqual(len(hashes), 1,
                f"Object {obj!r} serialization is non-deterministic")

    def test_deterministic_across_versions(self):
        for version in range(marshal.version + 1):
            for obj in [42, "hello", b"world"]:
                try:
                    hashes = set()
                    for _ in range(10):
                        result = marshal.dumps(obj, version)
                        hashes.add(hash_bytes(result))
                    self.assertEqual(len(hashes), 1,
                        f"Version {version}: Object {obj!r} serialization is non-deterministic")
                except ValueError:
                    pass


class TestExactTypeMatch(unittest.TestCase):
    def test_subclass_rejection(self):
        for typ in (int, float, complex):
            subtyp = type('subtyp', (typ,), {})
            with self.assertRaises(ValueError):
                marshal.dumps(subtyp())
        
        for typ in (tuple, list, dict, set, frozenset):
            subtyp = type('subtyp', (typ,), {})
            with self.assertRaises(ValueError):
                marshal.dumps(subtyp())


def run_tests():
    import io
    old_stdout = sys.stdout
    sys.stdout = io.StringIO()

    loader = unittest.TestLoader()
    suite = loader.loadTestsFromName(__name__)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    output = sys.stdout.getvalue()
    sys.stdout = old_stdout

    print('=' * 60)
    print('Member A Test Suite - Results Summary')
    print('=' * 60)
    print(f'Tests Run: {result.testsRun}')
    print(f'Failures: {len(result.failures)}')
    print(f'Errors: {len(result.errors)}')
    print(f'Skipped: {len(result.skipped)}')
    print(f'Passed: {result.testsRun - len(result.failures) - len(result.errors)}')
    print('=' * 60)

    if result.failures or result.errors:
        print('\nDetailed Error Information:')
        print(output[-4000:] if len(output) > 4000 else output)
    else:
        print('\n🎉 All Tests Passed!')

    return result


if __name__ == "__main__":
    run_tests()
