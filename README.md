# Python marshal Module Stability Test Suite

## Test Files Overview

| File Name | Test Content |
|-----------|-------------|
| `R1_R2_Test.py` | Determinism tests for basic scalar types (None, bool, int, str, bytes); integer boundary value tests (2^31, 2^63, etc.); string interning and small integer cache isolation tests |
| `R3_Test.py` | Float/complex number stability tests; NaN payload mutability tests; Unicode and byte scalar extension tests |
| `R4_Test.py` | Container type tests; set/frozenset non-determinism tests; large container memory boundary tests; non-determinism propagation in nested containers |
| `R5_Test.py` | Recursive structure tests; deep nesting boundary tests; unsupported object type exception handling; shared reference tests; marshal version parameter tests; invalid byte stream deserialization tests |
| `R6_Test.py` | Code object serialization tests; compilation optimization level tests; repeated compilation stability tests; cross-version code format tests; closure code object tests; async/NaN code object tests |

## Team Members & Responsibilities

| Member | Responsible Module |
|--------|-------------------|
| Xu Xinyi(member A) | R1, R2 (Scalar and Integer Tests) |
| Chen Yike(member B) | R3 (Float/Complex Tests) |
| Yang Gu(member C) | R4 (Container Type Tests) |
| Hu Jinyue(member D) | R5 (Recursive Structures & Exception Handling) |
| He Anqi(member E) | R6 (Code Objects & Cross-Platform Tests) |
