# 成员 B：跨平台 marshal 哈希比对

## Overall Result

All compared float/complex marshal hashes are identical across the tested platforms.

## Skipped Result Files

The following `*_results.json` files were not part of the float/complex suite and were excluded from this comparison:

- `member_b_all_darwin_arm64_py3_9_results.json`
- `scalar_binary_darwin_arm64_py3_9_results.json`
- `scalar_binary_linux_aarch64_py3_12_results.json`
- `scalar_binary_linux_x86_64_py3_12_results.json`

## darwin_arm64_py3_9_results (Darwin/arm64) vs darwin_results (Darwin/arm64)

| Case | System A Hash | System B Hash | Cross-platform Same | Note |
| --- | --- | --- | --- | --- |
| complex_inf_neg_inf | 16ffe3f0019c20865a65292d45049e5fa8f1c058d624d8d9ca60c06fd7fc7185 | 16ffe3f0019c20865a65292d45049e5fa8f1c058d624d8d9ca60c06fd7fc7185 | SAME | First marshal hash is identical |
| complex_nan_both | e1e3a81e18b46f75f6875063c865930f6c83cc875b54a359bc7f48a75851942a | e1e3a81e18b46f75f6875063c865930f6c83cc875b54a359bc7f48a75851942a | SAME | NaN-related case; First marshal hash is identical |
| complex_nan_imag | e146a4569769bc345bd4c478a6fbf7be401ce1ec409f12a5a5d73c65cdb299f9 | e146a4569769bc345bd4c478a6fbf7be401ce1ec409f12a5a5d73c65cdb299f9 | SAME | NaN-related case; First marshal hash is identical |
| complex_nan_real | cb8c7796e2953788906ddcf5dff7277efee4698b4f309292c49f1985557b1140 | cb8c7796e2953788906ddcf5dff7277efee4698b4f309292c49f1985557b1140 | SAME | NaN-related case; First marshal hash is identical |
| complex_payload_nan_imag | 012216faa4e8ae8ecfabe251b627080503fdb14ce7c4dbe9d634a40a5b84f9e8 | 012216faa4e8ae8ecfabe251b627080503fdb14ce7c4dbe9d634a40a5b84f9e8 | SAME | NaN-related case; First marshal hash is identical |
| complex_payload_nan_real | 1beb17130802d2f0fefe56ea3c31d81577cc2eeab4b4fa2ae98c9dadd5163045 | 1beb17130802d2f0fefe56ea3c31d81577cc2eeab4b4fa2ae98c9dadd5163045 | SAME | NaN-related case; First marshal hash is identical |
| complex_regular | 13f9d102452fbe198eb8b5cb55774896f74e8f27082755ee77815648d39f2aee | 13f9d102452fbe198eb8b5cb55774896f74e8f27082755ee77815648d39f2aee | SAME | First marshal hash is identical |
| complex_zero_neg_zero | ecc9d31e234cb555be59c308a16e7307008444fdec7e7af1a5e7d5f859268e51 | ecc9d31e234cb555be59c308a16e7307008444fdec7e7af1a5e7d5f859268e51 | SAME | First marshal hash is identical |
| float_huge_1e300 | 6ef4ab36a8fcc25428ca4fa5fd3cbe4326cb6a77a3aa95b8ab39f1c49a1856e5 | 6ef4ab36a8fcc25428ca4fa5fd3cbe4326cb6a77a3aa95b8ab39f1c49a1856e5 | SAME | First marshal hash is identical |
| float_math_nan | c0071368d2b0e5cb29b0995db32ea00ef9a3c215871dbabf0d4146930d1c7196 | c0071368d2b0e5cb29b0995db32ea00ef9a3c215871dbabf0d4146930d1c7196 | SAME | NaN-related case; First marshal hash is identical |
| float_nan_constructor | c0071368d2b0e5cb29b0995db32ea00ef9a3c215871dbabf0d4146930d1c7196 | c0071368d2b0e5cb29b0995db32ea00ef9a3c215871dbabf0d4146930d1c7196 | SAME | NaN-related case; First marshal hash is identical |
| float_nan_payload_0x7ff0000000000001 | 2f0de87ad7942c39db5b134b59b39c7412caba6b08eaf8e94e0a79ffb350d17e | 2f0de87ad7942c39db5b134b59b39c7412caba6b08eaf8e94e0a79ffb350d17e | SAME | NaN-related case; First marshal hash is identical |
| float_nan_payload_0x7ff8000000000001 | d46aba2832d3d50b093241faf925229d46e248e0a42cc47b39bb156d379421f9 | d46aba2832d3d50b093241faf925229d46e248e0a42cc47b39bb156d379421f9 | SAME | NaN-related case; First marshal hash is identical |
| float_nan_payload_0x7ff8000000000002 | f1c589f99c6e898331e5748e7d35bfc4b21a1c987f7626bb538a0cfcdcf5f74b | f1c589f99c6e898331e5748e7d35bfc4b21a1c987f7626bb538a0cfcdcf5f74b | SAME | NaN-related case; First marshal hash is identical |
| float_neg_inf | 860d99b42a646c71e28db195c6fdd2478e70455cb540732d1204ea023e3fb0cf | 860d99b42a646c71e28db195c6fdd2478e70455cb540732d1204ea023e3fb0cf | SAME | First marshal hash is identical |
| float_neg_one | e90fb050b711c19aec69b560ea01231514d62db4ad42f237f90b71def457f7e8 | e90fb050b711c19aec69b560ea01231514d62db4ad42f237f90b71def457f7e8 | SAME | First marshal hash is identical |
| float_neg_zero | 61d36befa08b84a6b58ddc977ad118100fb1e244e7be671d6f1e027ba585a163 | 61d36befa08b84a6b58ddc977ad118100fb1e244e7be671d6f1e027ba585a163 | SAME | First marshal hash is identical |
| float_pos_inf | a723a76079a60280dcdb2d7984a2adf4a0874e31b9518b30dfc0cfd9c3b53c54 | a723a76079a60280dcdb2d7984a2adf4a0874e31b9518b30dfc0cfd9c3b53c54 | SAME | First marshal hash is identical |
| float_pos_one | e574874a68d6058d6964c76836f36b4ddd75aee39f039c40fdad1b2a74361e46 | e574874a68d6058d6964c76836f36b4ddd75aee39f039c40fdad1b2a74361e46 | SAME | First marshal hash is identical |
| float_pos_zero | a7b2474c2b69133fff4c0515276a03bbf9d1c38d1d1f8c08bd5db478181398d6 | a7b2474c2b69133fff4c0515276a03bbf9d1c38d1d1f8c08bd5db478181398d6 | SAME | First marshal hash is identical |
| float_tiny_1e_minus_300 | d679077dca0189be07153975b6a6f0213b62cf2d2934903c49b1bc81c19bf939 | d679077dca0189be07153975b6a6f0213b62cf2d2934903c49b1bc81c19bf939 | SAME | First marshal hash is identical |
| recreated_complex_nan_both | e1e3a81e18b46f75f6875063c865930f6c83cc875b54a359bc7f48a75851942a | e1e3a81e18b46f75f6875063c865930f6c83cc875b54a359bc7f48a75851942a | SAME | NaN-related case; First marshal hash is identical |
| recreated_float_nan | c0071368d2b0e5cb29b0995db32ea00ef9a3c215871dbabf0d4146930d1c7196 | c0071368d2b0e5cb29b0995db32ea00ef9a3c215871dbabf0d4146930d1c7196 | SAME | NaN-related case; First marshal hash is identical |

## darwin_arm64_py3_9_results (Darwin/arm64) vs linux_aarch64_py3_12_results (Linux/aarch64)

| Case | System A Hash | System B Hash | Cross-platform Same | Note |
| --- | --- | --- | --- | --- |
| complex_inf_neg_inf | 16ffe3f0019c20865a65292d45049e5fa8f1c058d624d8d9ca60c06fd7fc7185 | 16ffe3f0019c20865a65292d45049e5fa8f1c058d624d8d9ca60c06fd7fc7185 | SAME | First marshal hash is identical |
| complex_nan_both | e1e3a81e18b46f75f6875063c865930f6c83cc875b54a359bc7f48a75851942a | e1e3a81e18b46f75f6875063c865930f6c83cc875b54a359bc7f48a75851942a | SAME | NaN-related case; First marshal hash is identical |
| complex_nan_imag | e146a4569769bc345bd4c478a6fbf7be401ce1ec409f12a5a5d73c65cdb299f9 | e146a4569769bc345bd4c478a6fbf7be401ce1ec409f12a5a5d73c65cdb299f9 | SAME | NaN-related case; First marshal hash is identical |
| complex_nan_real | cb8c7796e2953788906ddcf5dff7277efee4698b4f309292c49f1985557b1140 | cb8c7796e2953788906ddcf5dff7277efee4698b4f309292c49f1985557b1140 | SAME | NaN-related case; First marshal hash is identical |
| complex_payload_nan_imag | 012216faa4e8ae8ecfabe251b627080503fdb14ce7c4dbe9d634a40a5b84f9e8 | 012216faa4e8ae8ecfabe251b627080503fdb14ce7c4dbe9d634a40a5b84f9e8 | SAME | NaN-related case; First marshal hash is identical |
| complex_payload_nan_real | 1beb17130802d2f0fefe56ea3c31d81577cc2eeab4b4fa2ae98c9dadd5163045 | 1beb17130802d2f0fefe56ea3c31d81577cc2eeab4b4fa2ae98c9dadd5163045 | SAME | NaN-related case; First marshal hash is identical |
| complex_regular | 13f9d102452fbe198eb8b5cb55774896f74e8f27082755ee77815648d39f2aee | 13f9d102452fbe198eb8b5cb55774896f74e8f27082755ee77815648d39f2aee | SAME | First marshal hash is identical |
| complex_zero_neg_zero | ecc9d31e234cb555be59c308a16e7307008444fdec7e7af1a5e7d5f859268e51 | ecc9d31e234cb555be59c308a16e7307008444fdec7e7af1a5e7d5f859268e51 | SAME | First marshal hash is identical |
| float_huge_1e300 | 6ef4ab36a8fcc25428ca4fa5fd3cbe4326cb6a77a3aa95b8ab39f1c49a1856e5 | 6ef4ab36a8fcc25428ca4fa5fd3cbe4326cb6a77a3aa95b8ab39f1c49a1856e5 | SAME | First marshal hash is identical |
| float_math_nan | c0071368d2b0e5cb29b0995db32ea00ef9a3c215871dbabf0d4146930d1c7196 | c0071368d2b0e5cb29b0995db32ea00ef9a3c215871dbabf0d4146930d1c7196 | SAME | NaN-related case; First marshal hash is identical |
| float_nan_constructor | c0071368d2b0e5cb29b0995db32ea00ef9a3c215871dbabf0d4146930d1c7196 | c0071368d2b0e5cb29b0995db32ea00ef9a3c215871dbabf0d4146930d1c7196 | SAME | NaN-related case; First marshal hash is identical |
| float_nan_payload_0x7ff0000000000001 | 2f0de87ad7942c39db5b134b59b39c7412caba6b08eaf8e94e0a79ffb350d17e | 2f0de87ad7942c39db5b134b59b39c7412caba6b08eaf8e94e0a79ffb350d17e | SAME | NaN-related case; First marshal hash is identical |
| float_nan_payload_0x7ff8000000000001 | d46aba2832d3d50b093241faf925229d46e248e0a42cc47b39bb156d379421f9 | d46aba2832d3d50b093241faf925229d46e248e0a42cc47b39bb156d379421f9 | SAME | NaN-related case; First marshal hash is identical |
| float_nan_payload_0x7ff8000000000002 | f1c589f99c6e898331e5748e7d35bfc4b21a1c987f7626bb538a0cfcdcf5f74b | f1c589f99c6e898331e5748e7d35bfc4b21a1c987f7626bb538a0cfcdcf5f74b | SAME | NaN-related case; First marshal hash is identical |
| float_neg_inf | 860d99b42a646c71e28db195c6fdd2478e70455cb540732d1204ea023e3fb0cf | 860d99b42a646c71e28db195c6fdd2478e70455cb540732d1204ea023e3fb0cf | SAME | First marshal hash is identical |
| float_neg_one | e90fb050b711c19aec69b560ea01231514d62db4ad42f237f90b71def457f7e8 | e90fb050b711c19aec69b560ea01231514d62db4ad42f237f90b71def457f7e8 | SAME | First marshal hash is identical |
| float_neg_zero | 61d36befa08b84a6b58ddc977ad118100fb1e244e7be671d6f1e027ba585a163 | 61d36befa08b84a6b58ddc977ad118100fb1e244e7be671d6f1e027ba585a163 | SAME | First marshal hash is identical |
| float_pos_inf | a723a76079a60280dcdb2d7984a2adf4a0874e31b9518b30dfc0cfd9c3b53c54 | a723a76079a60280dcdb2d7984a2adf4a0874e31b9518b30dfc0cfd9c3b53c54 | SAME | First marshal hash is identical |
| float_pos_one | e574874a68d6058d6964c76836f36b4ddd75aee39f039c40fdad1b2a74361e46 | e574874a68d6058d6964c76836f36b4ddd75aee39f039c40fdad1b2a74361e46 | SAME | First marshal hash is identical |
| float_pos_zero | a7b2474c2b69133fff4c0515276a03bbf9d1c38d1d1f8c08bd5db478181398d6 | a7b2474c2b69133fff4c0515276a03bbf9d1c38d1d1f8c08bd5db478181398d6 | SAME | First marshal hash is identical |
| float_tiny_1e_minus_300 | d679077dca0189be07153975b6a6f0213b62cf2d2934903c49b1bc81c19bf939 | d679077dca0189be07153975b6a6f0213b62cf2d2934903c49b1bc81c19bf939 | SAME | First marshal hash is identical |
| recreated_complex_nan_both | e1e3a81e18b46f75f6875063c865930f6c83cc875b54a359bc7f48a75851942a | e1e3a81e18b46f75f6875063c865930f6c83cc875b54a359bc7f48a75851942a | SAME | NaN-related case; First marshal hash is identical |
| recreated_float_nan | c0071368d2b0e5cb29b0995db32ea00ef9a3c215871dbabf0d4146930d1c7196 | c0071368d2b0e5cb29b0995db32ea00ef9a3c215871dbabf0d4146930d1c7196 | SAME | NaN-related case; First marshal hash is identical |

## darwin_arm64_py3_9_results (Darwin/arm64) vs linux_x86_64_py3_12_results (Linux/x86_64)

| Case | System A Hash | System B Hash | Cross-platform Same | Note |
| --- | --- | --- | --- | --- |
| complex_inf_neg_inf | 16ffe3f0019c20865a65292d45049e5fa8f1c058d624d8d9ca60c06fd7fc7185 | 16ffe3f0019c20865a65292d45049e5fa8f1c058d624d8d9ca60c06fd7fc7185 | SAME | First marshal hash is identical |
| complex_nan_both | e1e3a81e18b46f75f6875063c865930f6c83cc875b54a359bc7f48a75851942a | e1e3a81e18b46f75f6875063c865930f6c83cc875b54a359bc7f48a75851942a | SAME | NaN-related case; First marshal hash is identical |
| complex_nan_imag | e146a4569769bc345bd4c478a6fbf7be401ce1ec409f12a5a5d73c65cdb299f9 | e146a4569769bc345bd4c478a6fbf7be401ce1ec409f12a5a5d73c65cdb299f9 | SAME | NaN-related case; First marshal hash is identical |
| complex_nan_real | cb8c7796e2953788906ddcf5dff7277efee4698b4f309292c49f1985557b1140 | cb8c7796e2953788906ddcf5dff7277efee4698b4f309292c49f1985557b1140 | SAME | NaN-related case; First marshal hash is identical |
| complex_payload_nan_imag | 012216faa4e8ae8ecfabe251b627080503fdb14ce7c4dbe9d634a40a5b84f9e8 | 012216faa4e8ae8ecfabe251b627080503fdb14ce7c4dbe9d634a40a5b84f9e8 | SAME | NaN-related case; First marshal hash is identical |
| complex_payload_nan_real | 1beb17130802d2f0fefe56ea3c31d81577cc2eeab4b4fa2ae98c9dadd5163045 | 1beb17130802d2f0fefe56ea3c31d81577cc2eeab4b4fa2ae98c9dadd5163045 | SAME | NaN-related case; First marshal hash is identical |
| complex_regular | 13f9d102452fbe198eb8b5cb55774896f74e8f27082755ee77815648d39f2aee | 13f9d102452fbe198eb8b5cb55774896f74e8f27082755ee77815648d39f2aee | SAME | First marshal hash is identical |
| complex_zero_neg_zero | ecc9d31e234cb555be59c308a16e7307008444fdec7e7af1a5e7d5f859268e51 | ecc9d31e234cb555be59c308a16e7307008444fdec7e7af1a5e7d5f859268e51 | SAME | First marshal hash is identical |
| float_huge_1e300 | 6ef4ab36a8fcc25428ca4fa5fd3cbe4326cb6a77a3aa95b8ab39f1c49a1856e5 | 6ef4ab36a8fcc25428ca4fa5fd3cbe4326cb6a77a3aa95b8ab39f1c49a1856e5 | SAME | First marshal hash is identical |
| float_math_nan | c0071368d2b0e5cb29b0995db32ea00ef9a3c215871dbabf0d4146930d1c7196 | c0071368d2b0e5cb29b0995db32ea00ef9a3c215871dbabf0d4146930d1c7196 | SAME | NaN-related case; First marshal hash is identical |
| float_nan_constructor | c0071368d2b0e5cb29b0995db32ea00ef9a3c215871dbabf0d4146930d1c7196 | c0071368d2b0e5cb29b0995db32ea00ef9a3c215871dbabf0d4146930d1c7196 | SAME | NaN-related case; First marshal hash is identical |
| float_nan_payload_0x7ff0000000000001 | 2f0de87ad7942c39db5b134b59b39c7412caba6b08eaf8e94e0a79ffb350d17e | 2f0de87ad7942c39db5b134b59b39c7412caba6b08eaf8e94e0a79ffb350d17e | SAME | NaN-related case; First marshal hash is identical |
| float_nan_payload_0x7ff8000000000001 | d46aba2832d3d50b093241faf925229d46e248e0a42cc47b39bb156d379421f9 | d46aba2832d3d50b093241faf925229d46e248e0a42cc47b39bb156d379421f9 | SAME | NaN-related case; First marshal hash is identical |
| float_nan_payload_0x7ff8000000000002 | f1c589f99c6e898331e5748e7d35bfc4b21a1c987f7626bb538a0cfcdcf5f74b | f1c589f99c6e898331e5748e7d35bfc4b21a1c987f7626bb538a0cfcdcf5f74b | SAME | NaN-related case; First marshal hash is identical |
| float_neg_inf | 860d99b42a646c71e28db195c6fdd2478e70455cb540732d1204ea023e3fb0cf | 860d99b42a646c71e28db195c6fdd2478e70455cb540732d1204ea023e3fb0cf | SAME | First marshal hash is identical |
| float_neg_one | e90fb050b711c19aec69b560ea01231514d62db4ad42f237f90b71def457f7e8 | e90fb050b711c19aec69b560ea01231514d62db4ad42f237f90b71def457f7e8 | SAME | First marshal hash is identical |
| float_neg_zero | 61d36befa08b84a6b58ddc977ad118100fb1e244e7be671d6f1e027ba585a163 | 61d36befa08b84a6b58ddc977ad118100fb1e244e7be671d6f1e027ba585a163 | SAME | First marshal hash is identical |
| float_pos_inf | a723a76079a60280dcdb2d7984a2adf4a0874e31b9518b30dfc0cfd9c3b53c54 | a723a76079a60280dcdb2d7984a2adf4a0874e31b9518b30dfc0cfd9c3b53c54 | SAME | First marshal hash is identical |
| float_pos_one | e574874a68d6058d6964c76836f36b4ddd75aee39f039c40fdad1b2a74361e46 | e574874a68d6058d6964c76836f36b4ddd75aee39f039c40fdad1b2a74361e46 | SAME | First marshal hash is identical |
| float_pos_zero | a7b2474c2b69133fff4c0515276a03bbf9d1c38d1d1f8c08bd5db478181398d6 | a7b2474c2b69133fff4c0515276a03bbf9d1c38d1d1f8c08bd5db478181398d6 | SAME | First marshal hash is identical |
| float_tiny_1e_minus_300 | d679077dca0189be07153975b6a6f0213b62cf2d2934903c49b1bc81c19bf939 | d679077dca0189be07153975b6a6f0213b62cf2d2934903c49b1bc81c19bf939 | SAME | First marshal hash is identical |
| recreated_complex_nan_both | e1e3a81e18b46f75f6875063c865930f6c83cc875b54a359bc7f48a75851942a | e1e3a81e18b46f75f6875063c865930f6c83cc875b54a359bc7f48a75851942a | SAME | NaN-related case; First marshal hash is identical |
| recreated_float_nan | c0071368d2b0e5cb29b0995db32ea00ef9a3c215871dbabf0d4146930d1c7196 | c0071368d2b0e5cb29b0995db32ea00ef9a3c215871dbabf0d4146930d1c7196 | SAME | NaN-related case; First marshal hash is identical |

## darwin_arm64_py3_9_results (Darwin/arm64) vs windows_amd64_py3_12_results (Windows/AMD64)

| Case | System A Hash | System B Hash | Cross-platform Same | Note |
| --- | --- | --- | --- | --- |
| complex_inf_neg_inf | 16ffe3f0019c20865a65292d45049e5fa8f1c058d624d8d9ca60c06fd7fc7185 | 16ffe3f0019c20865a65292d45049e5fa8f1c058d624d8d9ca60c06fd7fc7185 | SAME | First marshal hash is identical |
| complex_nan_both | e1e3a81e18b46f75f6875063c865930f6c83cc875b54a359bc7f48a75851942a | e1e3a81e18b46f75f6875063c865930f6c83cc875b54a359bc7f48a75851942a | SAME | NaN-related case; First marshal hash is identical |
| complex_nan_imag | e146a4569769bc345bd4c478a6fbf7be401ce1ec409f12a5a5d73c65cdb299f9 | e146a4569769bc345bd4c478a6fbf7be401ce1ec409f12a5a5d73c65cdb299f9 | SAME | NaN-related case; First marshal hash is identical |
| complex_nan_real | cb8c7796e2953788906ddcf5dff7277efee4698b4f309292c49f1985557b1140 | cb8c7796e2953788906ddcf5dff7277efee4698b4f309292c49f1985557b1140 | SAME | NaN-related case; First marshal hash is identical |
| complex_payload_nan_imag | 012216faa4e8ae8ecfabe251b627080503fdb14ce7c4dbe9d634a40a5b84f9e8 | 012216faa4e8ae8ecfabe251b627080503fdb14ce7c4dbe9d634a40a5b84f9e8 | SAME | NaN-related case; First marshal hash is identical |
| complex_payload_nan_real | 1beb17130802d2f0fefe56ea3c31d81577cc2eeab4b4fa2ae98c9dadd5163045 | 1beb17130802d2f0fefe56ea3c31d81577cc2eeab4b4fa2ae98c9dadd5163045 | SAME | NaN-related case; First marshal hash is identical |
| complex_regular | 13f9d102452fbe198eb8b5cb55774896f74e8f27082755ee77815648d39f2aee | 13f9d102452fbe198eb8b5cb55774896f74e8f27082755ee77815648d39f2aee | SAME | First marshal hash is identical |
| complex_zero_neg_zero | ecc9d31e234cb555be59c308a16e7307008444fdec7e7af1a5e7d5f859268e51 | ecc9d31e234cb555be59c308a16e7307008444fdec7e7af1a5e7d5f859268e51 | SAME | First marshal hash is identical |
| float_huge_1e300 | 6ef4ab36a8fcc25428ca4fa5fd3cbe4326cb6a77a3aa95b8ab39f1c49a1856e5 | 6ef4ab36a8fcc25428ca4fa5fd3cbe4326cb6a77a3aa95b8ab39f1c49a1856e5 | SAME | First marshal hash is identical |
| float_math_nan | c0071368d2b0e5cb29b0995db32ea00ef9a3c215871dbabf0d4146930d1c7196 | c0071368d2b0e5cb29b0995db32ea00ef9a3c215871dbabf0d4146930d1c7196 | SAME | NaN-related case; First marshal hash is identical |
| float_nan_constructor | c0071368d2b0e5cb29b0995db32ea00ef9a3c215871dbabf0d4146930d1c7196 | c0071368d2b0e5cb29b0995db32ea00ef9a3c215871dbabf0d4146930d1c7196 | SAME | NaN-related case; First marshal hash is identical |
| float_nan_payload_0x7ff0000000000001 | 2f0de87ad7942c39db5b134b59b39c7412caba6b08eaf8e94e0a79ffb350d17e | 2f0de87ad7942c39db5b134b59b39c7412caba6b08eaf8e94e0a79ffb350d17e | SAME | NaN-related case; First marshal hash is identical |
| float_nan_payload_0x7ff8000000000001 | d46aba2832d3d50b093241faf925229d46e248e0a42cc47b39bb156d379421f9 | d46aba2832d3d50b093241faf925229d46e248e0a42cc47b39bb156d379421f9 | SAME | NaN-related case; First marshal hash is identical |
| float_nan_payload_0x7ff8000000000002 | f1c589f99c6e898331e5748e7d35bfc4b21a1c987f7626bb538a0cfcdcf5f74b | f1c589f99c6e898331e5748e7d35bfc4b21a1c987f7626bb538a0cfcdcf5f74b | SAME | NaN-related case; First marshal hash is identical |
| float_neg_inf | 860d99b42a646c71e28db195c6fdd2478e70455cb540732d1204ea023e3fb0cf | 860d99b42a646c71e28db195c6fdd2478e70455cb540732d1204ea023e3fb0cf | SAME | First marshal hash is identical |
| float_neg_one | e90fb050b711c19aec69b560ea01231514d62db4ad42f237f90b71def457f7e8 | e90fb050b711c19aec69b560ea01231514d62db4ad42f237f90b71def457f7e8 | SAME | First marshal hash is identical |
| float_neg_zero | 61d36befa08b84a6b58ddc977ad118100fb1e244e7be671d6f1e027ba585a163 | 61d36befa08b84a6b58ddc977ad118100fb1e244e7be671d6f1e027ba585a163 | SAME | First marshal hash is identical |
| float_pos_inf | a723a76079a60280dcdb2d7984a2adf4a0874e31b9518b30dfc0cfd9c3b53c54 | a723a76079a60280dcdb2d7984a2adf4a0874e31b9518b30dfc0cfd9c3b53c54 | SAME | First marshal hash is identical |
| float_pos_one | e574874a68d6058d6964c76836f36b4ddd75aee39f039c40fdad1b2a74361e46 | e574874a68d6058d6964c76836f36b4ddd75aee39f039c40fdad1b2a74361e46 | SAME | First marshal hash is identical |
| float_pos_zero | a7b2474c2b69133fff4c0515276a03bbf9d1c38d1d1f8c08bd5db478181398d6 | a7b2474c2b69133fff4c0515276a03bbf9d1c38d1d1f8c08bd5db478181398d6 | SAME | First marshal hash is identical |
| float_tiny_1e_minus_300 | d679077dca0189be07153975b6a6f0213b62cf2d2934903c49b1bc81c19bf939 | d679077dca0189be07153975b6a6f0213b62cf2d2934903c49b1bc81c19bf939 | SAME | First marshal hash is identical |
| recreated_complex_nan_both | e1e3a81e18b46f75f6875063c865930f6c83cc875b54a359bc7f48a75851942a | e1e3a81e18b46f75f6875063c865930f6c83cc875b54a359bc7f48a75851942a | SAME | NaN-related case; First marshal hash is identical |
| recreated_float_nan | c0071368d2b0e5cb29b0995db32ea00ef9a3c215871dbabf0d4146930d1c7196 | c0071368d2b0e5cb29b0995db32ea00ef9a3c215871dbabf0d4146930d1c7196 | SAME | NaN-related case; First marshal hash is identical |

## darwin_results (Darwin/arm64) vs linux_aarch64_py3_12_results (Linux/aarch64)

| Case | System A Hash | System B Hash | Cross-platform Same | Note |
| --- | --- | --- | --- | --- |
| complex_inf_neg_inf | 16ffe3f0019c20865a65292d45049e5fa8f1c058d624d8d9ca60c06fd7fc7185 | 16ffe3f0019c20865a65292d45049e5fa8f1c058d624d8d9ca60c06fd7fc7185 | SAME | First marshal hash is identical |
| complex_nan_both | e1e3a81e18b46f75f6875063c865930f6c83cc875b54a359bc7f48a75851942a | e1e3a81e18b46f75f6875063c865930f6c83cc875b54a359bc7f48a75851942a | SAME | NaN-related case; First marshal hash is identical |
| complex_nan_imag | e146a4569769bc345bd4c478a6fbf7be401ce1ec409f12a5a5d73c65cdb299f9 | e146a4569769bc345bd4c478a6fbf7be401ce1ec409f12a5a5d73c65cdb299f9 | SAME | NaN-related case; First marshal hash is identical |
| complex_nan_real | cb8c7796e2953788906ddcf5dff7277efee4698b4f309292c49f1985557b1140 | cb8c7796e2953788906ddcf5dff7277efee4698b4f309292c49f1985557b1140 | SAME | NaN-related case; First marshal hash is identical |
| complex_payload_nan_imag | 012216faa4e8ae8ecfabe251b627080503fdb14ce7c4dbe9d634a40a5b84f9e8 | 012216faa4e8ae8ecfabe251b627080503fdb14ce7c4dbe9d634a40a5b84f9e8 | SAME | NaN-related case; First marshal hash is identical |
| complex_payload_nan_real | 1beb17130802d2f0fefe56ea3c31d81577cc2eeab4b4fa2ae98c9dadd5163045 | 1beb17130802d2f0fefe56ea3c31d81577cc2eeab4b4fa2ae98c9dadd5163045 | SAME | NaN-related case; First marshal hash is identical |
| complex_regular | 13f9d102452fbe198eb8b5cb55774896f74e8f27082755ee77815648d39f2aee | 13f9d102452fbe198eb8b5cb55774896f74e8f27082755ee77815648d39f2aee | SAME | First marshal hash is identical |
| complex_zero_neg_zero | ecc9d31e234cb555be59c308a16e7307008444fdec7e7af1a5e7d5f859268e51 | ecc9d31e234cb555be59c308a16e7307008444fdec7e7af1a5e7d5f859268e51 | SAME | First marshal hash is identical |
| float_huge_1e300 | 6ef4ab36a8fcc25428ca4fa5fd3cbe4326cb6a77a3aa95b8ab39f1c49a1856e5 | 6ef4ab36a8fcc25428ca4fa5fd3cbe4326cb6a77a3aa95b8ab39f1c49a1856e5 | SAME | First marshal hash is identical |
| float_math_nan | c0071368d2b0e5cb29b0995db32ea00ef9a3c215871dbabf0d4146930d1c7196 | c0071368d2b0e5cb29b0995db32ea00ef9a3c215871dbabf0d4146930d1c7196 | SAME | NaN-related case; First marshal hash is identical |
| float_nan_constructor | c0071368d2b0e5cb29b0995db32ea00ef9a3c215871dbabf0d4146930d1c7196 | c0071368d2b0e5cb29b0995db32ea00ef9a3c215871dbabf0d4146930d1c7196 | SAME | NaN-related case; First marshal hash is identical |
| float_nan_payload_0x7ff0000000000001 | 2f0de87ad7942c39db5b134b59b39c7412caba6b08eaf8e94e0a79ffb350d17e | 2f0de87ad7942c39db5b134b59b39c7412caba6b08eaf8e94e0a79ffb350d17e | SAME | NaN-related case; First marshal hash is identical |
| float_nan_payload_0x7ff8000000000001 | d46aba2832d3d50b093241faf925229d46e248e0a42cc47b39bb156d379421f9 | d46aba2832d3d50b093241faf925229d46e248e0a42cc47b39bb156d379421f9 | SAME | NaN-related case; First marshal hash is identical |
| float_nan_payload_0x7ff8000000000002 | f1c589f99c6e898331e5748e7d35bfc4b21a1c987f7626bb538a0cfcdcf5f74b | f1c589f99c6e898331e5748e7d35bfc4b21a1c987f7626bb538a0cfcdcf5f74b | SAME | NaN-related case; First marshal hash is identical |
| float_neg_inf | 860d99b42a646c71e28db195c6fdd2478e70455cb540732d1204ea023e3fb0cf | 860d99b42a646c71e28db195c6fdd2478e70455cb540732d1204ea023e3fb0cf | SAME | First marshal hash is identical |
| float_neg_one | e90fb050b711c19aec69b560ea01231514d62db4ad42f237f90b71def457f7e8 | e90fb050b711c19aec69b560ea01231514d62db4ad42f237f90b71def457f7e8 | SAME | First marshal hash is identical |
| float_neg_zero | 61d36befa08b84a6b58ddc977ad118100fb1e244e7be671d6f1e027ba585a163 | 61d36befa08b84a6b58ddc977ad118100fb1e244e7be671d6f1e027ba585a163 | SAME | First marshal hash is identical |
| float_pos_inf | a723a76079a60280dcdb2d7984a2adf4a0874e31b9518b30dfc0cfd9c3b53c54 | a723a76079a60280dcdb2d7984a2adf4a0874e31b9518b30dfc0cfd9c3b53c54 | SAME | First marshal hash is identical |
| float_pos_one | e574874a68d6058d6964c76836f36b4ddd75aee39f039c40fdad1b2a74361e46 | e574874a68d6058d6964c76836f36b4ddd75aee39f039c40fdad1b2a74361e46 | SAME | First marshal hash is identical |
| float_pos_zero | a7b2474c2b69133fff4c0515276a03bbf9d1c38d1d1f8c08bd5db478181398d6 | a7b2474c2b69133fff4c0515276a03bbf9d1c38d1d1f8c08bd5db478181398d6 | SAME | First marshal hash is identical |
| float_tiny_1e_minus_300 | d679077dca0189be07153975b6a6f0213b62cf2d2934903c49b1bc81c19bf939 | d679077dca0189be07153975b6a6f0213b62cf2d2934903c49b1bc81c19bf939 | SAME | First marshal hash is identical |
| recreated_complex_nan_both | e1e3a81e18b46f75f6875063c865930f6c83cc875b54a359bc7f48a75851942a | e1e3a81e18b46f75f6875063c865930f6c83cc875b54a359bc7f48a75851942a | SAME | NaN-related case; First marshal hash is identical |
| recreated_float_nan | c0071368d2b0e5cb29b0995db32ea00ef9a3c215871dbabf0d4146930d1c7196 | c0071368d2b0e5cb29b0995db32ea00ef9a3c215871dbabf0d4146930d1c7196 | SAME | NaN-related case; First marshal hash is identical |

## darwin_results (Darwin/arm64) vs linux_x86_64_py3_12_results (Linux/x86_64)

| Case | System A Hash | System B Hash | Cross-platform Same | Note |
| --- | --- | --- | --- | --- |
| complex_inf_neg_inf | 16ffe3f0019c20865a65292d45049e5fa8f1c058d624d8d9ca60c06fd7fc7185 | 16ffe3f0019c20865a65292d45049e5fa8f1c058d624d8d9ca60c06fd7fc7185 | SAME | First marshal hash is identical |
| complex_nan_both | e1e3a81e18b46f75f6875063c865930f6c83cc875b54a359bc7f48a75851942a | e1e3a81e18b46f75f6875063c865930f6c83cc875b54a359bc7f48a75851942a | SAME | NaN-related case; First marshal hash is identical |
| complex_nan_imag | e146a4569769bc345bd4c478a6fbf7be401ce1ec409f12a5a5d73c65cdb299f9 | e146a4569769bc345bd4c478a6fbf7be401ce1ec409f12a5a5d73c65cdb299f9 | SAME | NaN-related case; First marshal hash is identical |
| complex_nan_real | cb8c7796e2953788906ddcf5dff7277efee4698b4f309292c49f1985557b1140 | cb8c7796e2953788906ddcf5dff7277efee4698b4f309292c49f1985557b1140 | SAME | NaN-related case; First marshal hash is identical |
| complex_payload_nan_imag | 012216faa4e8ae8ecfabe251b627080503fdb14ce7c4dbe9d634a40a5b84f9e8 | 012216faa4e8ae8ecfabe251b627080503fdb14ce7c4dbe9d634a40a5b84f9e8 | SAME | NaN-related case; First marshal hash is identical |
| complex_payload_nan_real | 1beb17130802d2f0fefe56ea3c31d81577cc2eeab4b4fa2ae98c9dadd5163045 | 1beb17130802d2f0fefe56ea3c31d81577cc2eeab4b4fa2ae98c9dadd5163045 | SAME | NaN-related case; First marshal hash is identical |
| complex_regular | 13f9d102452fbe198eb8b5cb55774896f74e8f27082755ee77815648d39f2aee | 13f9d102452fbe198eb8b5cb55774896f74e8f27082755ee77815648d39f2aee | SAME | First marshal hash is identical |
| complex_zero_neg_zero | ecc9d31e234cb555be59c308a16e7307008444fdec7e7af1a5e7d5f859268e51 | ecc9d31e234cb555be59c308a16e7307008444fdec7e7af1a5e7d5f859268e51 | SAME | First marshal hash is identical |
| float_huge_1e300 | 6ef4ab36a8fcc25428ca4fa5fd3cbe4326cb6a77a3aa95b8ab39f1c49a1856e5 | 6ef4ab36a8fcc25428ca4fa5fd3cbe4326cb6a77a3aa95b8ab39f1c49a1856e5 | SAME | First marshal hash is identical |
| float_math_nan | c0071368d2b0e5cb29b0995db32ea00ef9a3c215871dbabf0d4146930d1c7196 | c0071368d2b0e5cb29b0995db32ea00ef9a3c215871dbabf0d4146930d1c7196 | SAME | NaN-related case; First marshal hash is identical |
| float_nan_constructor | c0071368d2b0e5cb29b0995db32ea00ef9a3c215871dbabf0d4146930d1c7196 | c0071368d2b0e5cb29b0995db32ea00ef9a3c215871dbabf0d4146930d1c7196 | SAME | NaN-related case; First marshal hash is identical |
| float_nan_payload_0x7ff0000000000001 | 2f0de87ad7942c39db5b134b59b39c7412caba6b08eaf8e94e0a79ffb350d17e | 2f0de87ad7942c39db5b134b59b39c7412caba6b08eaf8e94e0a79ffb350d17e | SAME | NaN-related case; First marshal hash is identical |
| float_nan_payload_0x7ff8000000000001 | d46aba2832d3d50b093241faf925229d46e248e0a42cc47b39bb156d379421f9 | d46aba2832d3d50b093241faf925229d46e248e0a42cc47b39bb156d379421f9 | SAME | NaN-related case; First marshal hash is identical |
| float_nan_payload_0x7ff8000000000002 | f1c589f99c6e898331e5748e7d35bfc4b21a1c987f7626bb538a0cfcdcf5f74b | f1c589f99c6e898331e5748e7d35bfc4b21a1c987f7626bb538a0cfcdcf5f74b | SAME | NaN-related case; First marshal hash is identical |
| float_neg_inf | 860d99b42a646c71e28db195c6fdd2478e70455cb540732d1204ea023e3fb0cf | 860d99b42a646c71e28db195c6fdd2478e70455cb540732d1204ea023e3fb0cf | SAME | First marshal hash is identical |
| float_neg_one | e90fb050b711c19aec69b560ea01231514d62db4ad42f237f90b71def457f7e8 | e90fb050b711c19aec69b560ea01231514d62db4ad42f237f90b71def457f7e8 | SAME | First marshal hash is identical |
| float_neg_zero | 61d36befa08b84a6b58ddc977ad118100fb1e244e7be671d6f1e027ba585a163 | 61d36befa08b84a6b58ddc977ad118100fb1e244e7be671d6f1e027ba585a163 | SAME | First marshal hash is identical |
| float_pos_inf | a723a76079a60280dcdb2d7984a2adf4a0874e31b9518b30dfc0cfd9c3b53c54 | a723a76079a60280dcdb2d7984a2adf4a0874e31b9518b30dfc0cfd9c3b53c54 | SAME | First marshal hash is identical |
| float_pos_one | e574874a68d6058d6964c76836f36b4ddd75aee39f039c40fdad1b2a74361e46 | e574874a68d6058d6964c76836f36b4ddd75aee39f039c40fdad1b2a74361e46 | SAME | First marshal hash is identical |
| float_pos_zero | a7b2474c2b69133fff4c0515276a03bbf9d1c38d1d1f8c08bd5db478181398d6 | a7b2474c2b69133fff4c0515276a03bbf9d1c38d1d1f8c08bd5db478181398d6 | SAME | First marshal hash is identical |
| float_tiny_1e_minus_300 | d679077dca0189be07153975b6a6f0213b62cf2d2934903c49b1bc81c19bf939 | d679077dca0189be07153975b6a6f0213b62cf2d2934903c49b1bc81c19bf939 | SAME | First marshal hash is identical |
| recreated_complex_nan_both | e1e3a81e18b46f75f6875063c865930f6c83cc875b54a359bc7f48a75851942a | e1e3a81e18b46f75f6875063c865930f6c83cc875b54a359bc7f48a75851942a | SAME | NaN-related case; First marshal hash is identical |
| recreated_float_nan | c0071368d2b0e5cb29b0995db32ea00ef9a3c215871dbabf0d4146930d1c7196 | c0071368d2b0e5cb29b0995db32ea00ef9a3c215871dbabf0d4146930d1c7196 | SAME | NaN-related case; First marshal hash is identical |

## darwin_results (Darwin/arm64) vs windows_amd64_py3_12_results (Windows/AMD64)

| Case | System A Hash | System B Hash | Cross-platform Same | Note |
| --- | --- | --- | --- | --- |
| complex_inf_neg_inf | 16ffe3f0019c20865a65292d45049e5fa8f1c058d624d8d9ca60c06fd7fc7185 | 16ffe3f0019c20865a65292d45049e5fa8f1c058d624d8d9ca60c06fd7fc7185 | SAME | First marshal hash is identical |
| complex_nan_both | e1e3a81e18b46f75f6875063c865930f6c83cc875b54a359bc7f48a75851942a | e1e3a81e18b46f75f6875063c865930f6c83cc875b54a359bc7f48a75851942a | SAME | NaN-related case; First marshal hash is identical |
| complex_nan_imag | e146a4569769bc345bd4c478a6fbf7be401ce1ec409f12a5a5d73c65cdb299f9 | e146a4569769bc345bd4c478a6fbf7be401ce1ec409f12a5a5d73c65cdb299f9 | SAME | NaN-related case; First marshal hash is identical |
| complex_nan_real | cb8c7796e2953788906ddcf5dff7277efee4698b4f309292c49f1985557b1140 | cb8c7796e2953788906ddcf5dff7277efee4698b4f309292c49f1985557b1140 | SAME | NaN-related case; First marshal hash is identical |
| complex_payload_nan_imag | 012216faa4e8ae8ecfabe251b627080503fdb14ce7c4dbe9d634a40a5b84f9e8 | 012216faa4e8ae8ecfabe251b627080503fdb14ce7c4dbe9d634a40a5b84f9e8 | SAME | NaN-related case; First marshal hash is identical |
| complex_payload_nan_real | 1beb17130802d2f0fefe56ea3c31d81577cc2eeab4b4fa2ae98c9dadd5163045 | 1beb17130802d2f0fefe56ea3c31d81577cc2eeab4b4fa2ae98c9dadd5163045 | SAME | NaN-related case; First marshal hash is identical |
| complex_regular | 13f9d102452fbe198eb8b5cb55774896f74e8f27082755ee77815648d39f2aee | 13f9d102452fbe198eb8b5cb55774896f74e8f27082755ee77815648d39f2aee | SAME | First marshal hash is identical |
| complex_zero_neg_zero | ecc9d31e234cb555be59c308a16e7307008444fdec7e7af1a5e7d5f859268e51 | ecc9d31e234cb555be59c308a16e7307008444fdec7e7af1a5e7d5f859268e51 | SAME | First marshal hash is identical |
| float_huge_1e300 | 6ef4ab36a8fcc25428ca4fa5fd3cbe4326cb6a77a3aa95b8ab39f1c49a1856e5 | 6ef4ab36a8fcc25428ca4fa5fd3cbe4326cb6a77a3aa95b8ab39f1c49a1856e5 | SAME | First marshal hash is identical |
| float_math_nan | c0071368d2b0e5cb29b0995db32ea00ef9a3c215871dbabf0d4146930d1c7196 | c0071368d2b0e5cb29b0995db32ea00ef9a3c215871dbabf0d4146930d1c7196 | SAME | NaN-related case; First marshal hash is identical |
| float_nan_constructor | c0071368d2b0e5cb29b0995db32ea00ef9a3c215871dbabf0d4146930d1c7196 | c0071368d2b0e5cb29b0995db32ea00ef9a3c215871dbabf0d4146930d1c7196 | SAME | NaN-related case; First marshal hash is identical |
| float_nan_payload_0x7ff0000000000001 | 2f0de87ad7942c39db5b134b59b39c7412caba6b08eaf8e94e0a79ffb350d17e | 2f0de87ad7942c39db5b134b59b39c7412caba6b08eaf8e94e0a79ffb350d17e | SAME | NaN-related case; First marshal hash is identical |
| float_nan_payload_0x7ff8000000000001 | d46aba2832d3d50b093241faf925229d46e248e0a42cc47b39bb156d379421f9 | d46aba2832d3d50b093241faf925229d46e248e0a42cc47b39bb156d379421f9 | SAME | NaN-related case; First marshal hash is identical |
| float_nan_payload_0x7ff8000000000002 | f1c589f99c6e898331e5748e7d35bfc4b21a1c987f7626bb538a0cfcdcf5f74b | f1c589f99c6e898331e5748e7d35bfc4b21a1c987f7626bb538a0cfcdcf5f74b | SAME | NaN-related case; First marshal hash is identical |
| float_neg_inf | 860d99b42a646c71e28db195c6fdd2478e70455cb540732d1204ea023e3fb0cf | 860d99b42a646c71e28db195c6fdd2478e70455cb540732d1204ea023e3fb0cf | SAME | First marshal hash is identical |
| float_neg_one | e90fb050b711c19aec69b560ea01231514d62db4ad42f237f90b71def457f7e8 | e90fb050b711c19aec69b560ea01231514d62db4ad42f237f90b71def457f7e8 | SAME | First marshal hash is identical |
| float_neg_zero | 61d36befa08b84a6b58ddc977ad118100fb1e244e7be671d6f1e027ba585a163 | 61d36befa08b84a6b58ddc977ad118100fb1e244e7be671d6f1e027ba585a163 | SAME | First marshal hash is identical |
| float_pos_inf | a723a76079a60280dcdb2d7984a2adf4a0874e31b9518b30dfc0cfd9c3b53c54 | a723a76079a60280dcdb2d7984a2adf4a0874e31b9518b30dfc0cfd9c3b53c54 | SAME | First marshal hash is identical |
| float_pos_one | e574874a68d6058d6964c76836f36b4ddd75aee39f039c40fdad1b2a74361e46 | e574874a68d6058d6964c76836f36b4ddd75aee39f039c40fdad1b2a74361e46 | SAME | First marshal hash is identical |
| float_pos_zero | a7b2474c2b69133fff4c0515276a03bbf9d1c38d1d1f8c08bd5db478181398d6 | a7b2474c2b69133fff4c0515276a03bbf9d1c38d1d1f8c08bd5db478181398d6 | SAME | First marshal hash is identical |
| float_tiny_1e_minus_300 | d679077dca0189be07153975b6a6f0213b62cf2d2934903c49b1bc81c19bf939 | d679077dca0189be07153975b6a6f0213b62cf2d2934903c49b1bc81c19bf939 | SAME | First marshal hash is identical |
| recreated_complex_nan_both | e1e3a81e18b46f75f6875063c865930f6c83cc875b54a359bc7f48a75851942a | e1e3a81e18b46f75f6875063c865930f6c83cc875b54a359bc7f48a75851942a | SAME | NaN-related case; First marshal hash is identical |
| recreated_float_nan | c0071368d2b0e5cb29b0995db32ea00ef9a3c215871dbabf0d4146930d1c7196 | c0071368d2b0e5cb29b0995db32ea00ef9a3c215871dbabf0d4146930d1c7196 | SAME | NaN-related case; First marshal hash is identical |

## linux_aarch64_py3_12_results (Linux/aarch64) vs linux_x86_64_py3_12_results (Linux/x86_64)

| Case | System A Hash | System B Hash | Cross-platform Same | Note |
| --- | --- | --- | --- | --- |
| complex_inf_neg_inf | 16ffe3f0019c20865a65292d45049e5fa8f1c058d624d8d9ca60c06fd7fc7185 | 16ffe3f0019c20865a65292d45049e5fa8f1c058d624d8d9ca60c06fd7fc7185 | SAME | First marshal hash is identical |
| complex_nan_both | e1e3a81e18b46f75f6875063c865930f6c83cc875b54a359bc7f48a75851942a | e1e3a81e18b46f75f6875063c865930f6c83cc875b54a359bc7f48a75851942a | SAME | NaN-related case; First marshal hash is identical |
| complex_nan_imag | e146a4569769bc345bd4c478a6fbf7be401ce1ec409f12a5a5d73c65cdb299f9 | e146a4569769bc345bd4c478a6fbf7be401ce1ec409f12a5a5d73c65cdb299f9 | SAME | NaN-related case; First marshal hash is identical |
| complex_nan_real | cb8c7796e2953788906ddcf5dff7277efee4698b4f309292c49f1985557b1140 | cb8c7796e2953788906ddcf5dff7277efee4698b4f309292c49f1985557b1140 | SAME | NaN-related case; First marshal hash is identical |
| complex_payload_nan_imag | 012216faa4e8ae8ecfabe251b627080503fdb14ce7c4dbe9d634a40a5b84f9e8 | 012216faa4e8ae8ecfabe251b627080503fdb14ce7c4dbe9d634a40a5b84f9e8 | SAME | NaN-related case; First marshal hash is identical |
| complex_payload_nan_real | 1beb17130802d2f0fefe56ea3c31d81577cc2eeab4b4fa2ae98c9dadd5163045 | 1beb17130802d2f0fefe56ea3c31d81577cc2eeab4b4fa2ae98c9dadd5163045 | SAME | NaN-related case; First marshal hash is identical |
| complex_regular | 13f9d102452fbe198eb8b5cb55774896f74e8f27082755ee77815648d39f2aee | 13f9d102452fbe198eb8b5cb55774896f74e8f27082755ee77815648d39f2aee | SAME | First marshal hash is identical |
| complex_zero_neg_zero | ecc9d31e234cb555be59c308a16e7307008444fdec7e7af1a5e7d5f859268e51 | ecc9d31e234cb555be59c308a16e7307008444fdec7e7af1a5e7d5f859268e51 | SAME | First marshal hash is identical |
| float_huge_1e300 | 6ef4ab36a8fcc25428ca4fa5fd3cbe4326cb6a77a3aa95b8ab39f1c49a1856e5 | 6ef4ab36a8fcc25428ca4fa5fd3cbe4326cb6a77a3aa95b8ab39f1c49a1856e5 | SAME | First marshal hash is identical |
| float_math_nan | c0071368d2b0e5cb29b0995db32ea00ef9a3c215871dbabf0d4146930d1c7196 | c0071368d2b0e5cb29b0995db32ea00ef9a3c215871dbabf0d4146930d1c7196 | SAME | NaN-related case; First marshal hash is identical |
| float_nan_constructor | c0071368d2b0e5cb29b0995db32ea00ef9a3c215871dbabf0d4146930d1c7196 | c0071368d2b0e5cb29b0995db32ea00ef9a3c215871dbabf0d4146930d1c7196 | SAME | NaN-related case; First marshal hash is identical |
| float_nan_payload_0x7ff0000000000001 | 2f0de87ad7942c39db5b134b59b39c7412caba6b08eaf8e94e0a79ffb350d17e | 2f0de87ad7942c39db5b134b59b39c7412caba6b08eaf8e94e0a79ffb350d17e | SAME | NaN-related case; First marshal hash is identical |
| float_nan_payload_0x7ff8000000000001 | d46aba2832d3d50b093241faf925229d46e248e0a42cc47b39bb156d379421f9 | d46aba2832d3d50b093241faf925229d46e248e0a42cc47b39bb156d379421f9 | SAME | NaN-related case; First marshal hash is identical |
| float_nan_payload_0x7ff8000000000002 | f1c589f99c6e898331e5748e7d35bfc4b21a1c987f7626bb538a0cfcdcf5f74b | f1c589f99c6e898331e5748e7d35bfc4b21a1c987f7626bb538a0cfcdcf5f74b | SAME | NaN-related case; First marshal hash is identical |
| float_neg_inf | 860d99b42a646c71e28db195c6fdd2478e70455cb540732d1204ea023e3fb0cf | 860d99b42a646c71e28db195c6fdd2478e70455cb540732d1204ea023e3fb0cf | SAME | First marshal hash is identical |
| float_neg_one | e90fb050b711c19aec69b560ea01231514d62db4ad42f237f90b71def457f7e8 | e90fb050b711c19aec69b560ea01231514d62db4ad42f237f90b71def457f7e8 | SAME | First marshal hash is identical |
| float_neg_zero | 61d36befa08b84a6b58ddc977ad118100fb1e244e7be671d6f1e027ba585a163 | 61d36befa08b84a6b58ddc977ad118100fb1e244e7be671d6f1e027ba585a163 | SAME | First marshal hash is identical |
| float_pos_inf | a723a76079a60280dcdb2d7984a2adf4a0874e31b9518b30dfc0cfd9c3b53c54 | a723a76079a60280dcdb2d7984a2adf4a0874e31b9518b30dfc0cfd9c3b53c54 | SAME | First marshal hash is identical |
| float_pos_one | e574874a68d6058d6964c76836f36b4ddd75aee39f039c40fdad1b2a74361e46 | e574874a68d6058d6964c76836f36b4ddd75aee39f039c40fdad1b2a74361e46 | SAME | First marshal hash is identical |
| float_pos_zero | a7b2474c2b69133fff4c0515276a03bbf9d1c38d1d1f8c08bd5db478181398d6 | a7b2474c2b69133fff4c0515276a03bbf9d1c38d1d1f8c08bd5db478181398d6 | SAME | First marshal hash is identical |
| float_tiny_1e_minus_300 | d679077dca0189be07153975b6a6f0213b62cf2d2934903c49b1bc81c19bf939 | d679077dca0189be07153975b6a6f0213b62cf2d2934903c49b1bc81c19bf939 | SAME | First marshal hash is identical |
| recreated_complex_nan_both | e1e3a81e18b46f75f6875063c865930f6c83cc875b54a359bc7f48a75851942a | e1e3a81e18b46f75f6875063c865930f6c83cc875b54a359bc7f48a75851942a | SAME | NaN-related case; First marshal hash is identical |
| recreated_float_nan | c0071368d2b0e5cb29b0995db32ea00ef9a3c215871dbabf0d4146930d1c7196 | c0071368d2b0e5cb29b0995db32ea00ef9a3c215871dbabf0d4146930d1c7196 | SAME | NaN-related case; First marshal hash is identical |

## linux_aarch64_py3_12_results (Linux/aarch64) vs windows_amd64_py3_12_results (Windows/AMD64)

| Case | System A Hash | System B Hash | Cross-platform Same | Note |
| --- | --- | --- | --- | --- |
| complex_inf_neg_inf | 16ffe3f0019c20865a65292d45049e5fa8f1c058d624d8d9ca60c06fd7fc7185 | 16ffe3f0019c20865a65292d45049e5fa8f1c058d624d8d9ca60c06fd7fc7185 | SAME | First marshal hash is identical |
| complex_nan_both | e1e3a81e18b46f75f6875063c865930f6c83cc875b54a359bc7f48a75851942a | e1e3a81e18b46f75f6875063c865930f6c83cc875b54a359bc7f48a75851942a | SAME | NaN-related case; First marshal hash is identical |
| complex_nan_imag | e146a4569769bc345bd4c478a6fbf7be401ce1ec409f12a5a5d73c65cdb299f9 | e146a4569769bc345bd4c478a6fbf7be401ce1ec409f12a5a5d73c65cdb299f9 | SAME | NaN-related case; First marshal hash is identical |
| complex_nan_real | cb8c7796e2953788906ddcf5dff7277efee4698b4f309292c49f1985557b1140 | cb8c7796e2953788906ddcf5dff7277efee4698b4f309292c49f1985557b1140 | SAME | NaN-related case; First marshal hash is identical |
| complex_payload_nan_imag | 012216faa4e8ae8ecfabe251b627080503fdb14ce7c4dbe9d634a40a5b84f9e8 | 012216faa4e8ae8ecfabe251b627080503fdb14ce7c4dbe9d634a40a5b84f9e8 | SAME | NaN-related case; First marshal hash is identical |
| complex_payload_nan_real | 1beb17130802d2f0fefe56ea3c31d81577cc2eeab4b4fa2ae98c9dadd5163045 | 1beb17130802d2f0fefe56ea3c31d81577cc2eeab4b4fa2ae98c9dadd5163045 | SAME | NaN-related case; First marshal hash is identical |
| complex_regular | 13f9d102452fbe198eb8b5cb55774896f74e8f27082755ee77815648d39f2aee | 13f9d102452fbe198eb8b5cb55774896f74e8f27082755ee77815648d39f2aee | SAME | First marshal hash is identical |
| complex_zero_neg_zero | ecc9d31e234cb555be59c308a16e7307008444fdec7e7af1a5e7d5f859268e51 | ecc9d31e234cb555be59c308a16e7307008444fdec7e7af1a5e7d5f859268e51 | SAME | First marshal hash is identical |
| float_huge_1e300 | 6ef4ab36a8fcc25428ca4fa5fd3cbe4326cb6a77a3aa95b8ab39f1c49a1856e5 | 6ef4ab36a8fcc25428ca4fa5fd3cbe4326cb6a77a3aa95b8ab39f1c49a1856e5 | SAME | First marshal hash is identical |
| float_math_nan | c0071368d2b0e5cb29b0995db32ea00ef9a3c215871dbabf0d4146930d1c7196 | c0071368d2b0e5cb29b0995db32ea00ef9a3c215871dbabf0d4146930d1c7196 | SAME | NaN-related case; First marshal hash is identical |
| float_nan_constructor | c0071368d2b0e5cb29b0995db32ea00ef9a3c215871dbabf0d4146930d1c7196 | c0071368d2b0e5cb29b0995db32ea00ef9a3c215871dbabf0d4146930d1c7196 | SAME | NaN-related case; First marshal hash is identical |
| float_nan_payload_0x7ff0000000000001 | 2f0de87ad7942c39db5b134b59b39c7412caba6b08eaf8e94e0a79ffb350d17e | 2f0de87ad7942c39db5b134b59b39c7412caba6b08eaf8e94e0a79ffb350d17e | SAME | NaN-related case; First marshal hash is identical |
| float_nan_payload_0x7ff8000000000001 | d46aba2832d3d50b093241faf925229d46e248e0a42cc47b39bb156d379421f9 | d46aba2832d3d50b093241faf925229d46e248e0a42cc47b39bb156d379421f9 | SAME | NaN-related case; First marshal hash is identical |
| float_nan_payload_0x7ff8000000000002 | f1c589f99c6e898331e5748e7d35bfc4b21a1c987f7626bb538a0cfcdcf5f74b | f1c589f99c6e898331e5748e7d35bfc4b21a1c987f7626bb538a0cfcdcf5f74b | SAME | NaN-related case; First marshal hash is identical |
| float_neg_inf | 860d99b42a646c71e28db195c6fdd2478e70455cb540732d1204ea023e3fb0cf | 860d99b42a646c71e28db195c6fdd2478e70455cb540732d1204ea023e3fb0cf | SAME | First marshal hash is identical |
| float_neg_one | e90fb050b711c19aec69b560ea01231514d62db4ad42f237f90b71def457f7e8 | e90fb050b711c19aec69b560ea01231514d62db4ad42f237f90b71def457f7e8 | SAME | First marshal hash is identical |
| float_neg_zero | 61d36befa08b84a6b58ddc977ad118100fb1e244e7be671d6f1e027ba585a163 | 61d36befa08b84a6b58ddc977ad118100fb1e244e7be671d6f1e027ba585a163 | SAME | First marshal hash is identical |
| float_pos_inf | a723a76079a60280dcdb2d7984a2adf4a0874e31b9518b30dfc0cfd9c3b53c54 | a723a76079a60280dcdb2d7984a2adf4a0874e31b9518b30dfc0cfd9c3b53c54 | SAME | First marshal hash is identical |
| float_pos_one | e574874a68d6058d6964c76836f36b4ddd75aee39f039c40fdad1b2a74361e46 | e574874a68d6058d6964c76836f36b4ddd75aee39f039c40fdad1b2a74361e46 | SAME | First marshal hash is identical |
| float_pos_zero | a7b2474c2b69133fff4c0515276a03bbf9d1c38d1d1f8c08bd5db478181398d6 | a7b2474c2b69133fff4c0515276a03bbf9d1c38d1d1f8c08bd5db478181398d6 | SAME | First marshal hash is identical |
| float_tiny_1e_minus_300 | d679077dca0189be07153975b6a6f0213b62cf2d2934903c49b1bc81c19bf939 | d679077dca0189be07153975b6a6f0213b62cf2d2934903c49b1bc81c19bf939 | SAME | First marshal hash is identical |
| recreated_complex_nan_both | e1e3a81e18b46f75f6875063c865930f6c83cc875b54a359bc7f48a75851942a | e1e3a81e18b46f75f6875063c865930f6c83cc875b54a359bc7f48a75851942a | SAME | NaN-related case; First marshal hash is identical |
| recreated_float_nan | c0071368d2b0e5cb29b0995db32ea00ef9a3c215871dbabf0d4146930d1c7196 | c0071368d2b0e5cb29b0995db32ea00ef9a3c215871dbabf0d4146930d1c7196 | SAME | NaN-related case; First marshal hash is identical |

## linux_x86_64_py3_12_results (Linux/x86_64) vs windows_amd64_py3_12_results (Windows/AMD64)

| Case | System A Hash | System B Hash | Cross-platform Same | Note |
| --- | --- | --- | --- | --- |
| complex_inf_neg_inf | 16ffe3f0019c20865a65292d45049e5fa8f1c058d624d8d9ca60c06fd7fc7185 | 16ffe3f0019c20865a65292d45049e5fa8f1c058d624d8d9ca60c06fd7fc7185 | SAME | First marshal hash is identical |
| complex_nan_both | e1e3a81e18b46f75f6875063c865930f6c83cc875b54a359bc7f48a75851942a | e1e3a81e18b46f75f6875063c865930f6c83cc875b54a359bc7f48a75851942a | SAME | NaN-related case; First marshal hash is identical |
| complex_nan_imag | e146a4569769bc345bd4c478a6fbf7be401ce1ec409f12a5a5d73c65cdb299f9 | e146a4569769bc345bd4c478a6fbf7be401ce1ec409f12a5a5d73c65cdb299f9 | SAME | NaN-related case; First marshal hash is identical |
| complex_nan_real | cb8c7796e2953788906ddcf5dff7277efee4698b4f309292c49f1985557b1140 | cb8c7796e2953788906ddcf5dff7277efee4698b4f309292c49f1985557b1140 | SAME | NaN-related case; First marshal hash is identical |
| complex_payload_nan_imag | 012216faa4e8ae8ecfabe251b627080503fdb14ce7c4dbe9d634a40a5b84f9e8 | 012216faa4e8ae8ecfabe251b627080503fdb14ce7c4dbe9d634a40a5b84f9e8 | SAME | NaN-related case; First marshal hash is identical |
| complex_payload_nan_real | 1beb17130802d2f0fefe56ea3c31d81577cc2eeab4b4fa2ae98c9dadd5163045 | 1beb17130802d2f0fefe56ea3c31d81577cc2eeab4b4fa2ae98c9dadd5163045 | SAME | NaN-related case; First marshal hash is identical |
| complex_regular | 13f9d102452fbe198eb8b5cb55774896f74e8f27082755ee77815648d39f2aee | 13f9d102452fbe198eb8b5cb55774896f74e8f27082755ee77815648d39f2aee | SAME | First marshal hash is identical |
| complex_zero_neg_zero | ecc9d31e234cb555be59c308a16e7307008444fdec7e7af1a5e7d5f859268e51 | ecc9d31e234cb555be59c308a16e7307008444fdec7e7af1a5e7d5f859268e51 | SAME | First marshal hash is identical |
| float_huge_1e300 | 6ef4ab36a8fcc25428ca4fa5fd3cbe4326cb6a77a3aa95b8ab39f1c49a1856e5 | 6ef4ab36a8fcc25428ca4fa5fd3cbe4326cb6a77a3aa95b8ab39f1c49a1856e5 | SAME | First marshal hash is identical |
| float_math_nan | c0071368d2b0e5cb29b0995db32ea00ef9a3c215871dbabf0d4146930d1c7196 | c0071368d2b0e5cb29b0995db32ea00ef9a3c215871dbabf0d4146930d1c7196 | SAME | NaN-related case; First marshal hash is identical |
| float_nan_constructor | c0071368d2b0e5cb29b0995db32ea00ef9a3c215871dbabf0d4146930d1c7196 | c0071368d2b0e5cb29b0995db32ea00ef9a3c215871dbabf0d4146930d1c7196 | SAME | NaN-related case; First marshal hash is identical |
| float_nan_payload_0x7ff0000000000001 | 2f0de87ad7942c39db5b134b59b39c7412caba6b08eaf8e94e0a79ffb350d17e | 2f0de87ad7942c39db5b134b59b39c7412caba6b08eaf8e94e0a79ffb350d17e | SAME | NaN-related case; First marshal hash is identical |
| float_nan_payload_0x7ff8000000000001 | d46aba2832d3d50b093241faf925229d46e248e0a42cc47b39bb156d379421f9 | d46aba2832d3d50b093241faf925229d46e248e0a42cc47b39bb156d379421f9 | SAME | NaN-related case; First marshal hash is identical |
| float_nan_payload_0x7ff8000000000002 | f1c589f99c6e898331e5748e7d35bfc4b21a1c987f7626bb538a0cfcdcf5f74b | f1c589f99c6e898331e5748e7d35bfc4b21a1c987f7626bb538a0cfcdcf5f74b | SAME | NaN-related case; First marshal hash is identical |
| float_neg_inf | 860d99b42a646c71e28db195c6fdd2478e70455cb540732d1204ea023e3fb0cf | 860d99b42a646c71e28db195c6fdd2478e70455cb540732d1204ea023e3fb0cf | SAME | First marshal hash is identical |
| float_neg_one | e90fb050b711c19aec69b560ea01231514d62db4ad42f237f90b71def457f7e8 | e90fb050b711c19aec69b560ea01231514d62db4ad42f237f90b71def457f7e8 | SAME | First marshal hash is identical |
| float_neg_zero | 61d36befa08b84a6b58ddc977ad118100fb1e244e7be671d6f1e027ba585a163 | 61d36befa08b84a6b58ddc977ad118100fb1e244e7be671d6f1e027ba585a163 | SAME | First marshal hash is identical |
| float_pos_inf | a723a76079a60280dcdb2d7984a2adf4a0874e31b9518b30dfc0cfd9c3b53c54 | a723a76079a60280dcdb2d7984a2adf4a0874e31b9518b30dfc0cfd9c3b53c54 | SAME | First marshal hash is identical |
| float_pos_one | e574874a68d6058d6964c76836f36b4ddd75aee39f039c40fdad1b2a74361e46 | e574874a68d6058d6964c76836f36b4ddd75aee39f039c40fdad1b2a74361e46 | SAME | First marshal hash is identical |
| float_pos_zero | a7b2474c2b69133fff4c0515276a03bbf9d1c38d1d1f8c08bd5db478181398d6 | a7b2474c2b69133fff4c0515276a03bbf9d1c38d1d1f8c08bd5db478181398d6 | SAME | First marshal hash is identical |
| float_tiny_1e_minus_300 | d679077dca0189be07153975b6a6f0213b62cf2d2934903c49b1bc81c19bf939 | d679077dca0189be07153975b6a6f0213b62cf2d2934903c49b1bc81c19bf939 | SAME | First marshal hash is identical |
| recreated_complex_nan_both | e1e3a81e18b46f75f6875063c865930f6c83cc875b54a359bc7f48a75851942a | e1e3a81e18b46f75f6875063c865930f6c83cc875b54a359bc7f48a75851942a | SAME | NaN-related case; First marshal hash is identical |
| recreated_float_nan | c0071368d2b0e5cb29b0995db32ea00ef9a3c215871dbabf0d4146930d1c7196 | c0071368d2b0e5cb29b0995db32ea00ef9a3c215871dbabf0d4146930d1c7196 | SAME | NaN-related case; First marshal hash is identical |
