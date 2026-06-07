#!/usr/bin/env python3
import unittest
import io
import sys

def main():
    old_stdout = sys.stdout
    sys.stdout = io.StringIO()

    loader = unittest.TestLoader()
    suite = loader.discover('.', pattern='test_member_a.py')
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

if __name__ == '__main__':
    main()
