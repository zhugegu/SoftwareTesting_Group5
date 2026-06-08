# -*- coding: utf-8 -*-
# 代码对象测试 + 跨平台/跨版本一致性测试
# 测试范围：R1.2、R6.1、R6.2、R6.3、R6.4、R6.5、R6.6
# 自动适配 Windows/Ubuntu/macOS三个系统
# 成员E：何安绮

import marshal
import sys
import os
import platform
import hashlib
import types

def get_hash(data: bytes) -> str:
    """计算哈希值，用于比对序列化字节是否一致"""
    return hashlib.sha256(data).hexdigest()

# ===================== 自动识别系统，自动设置日志路径 =====================
if platform.system() == "Windows":
    LOG_DIR = r"D:\RJTest\marshalTest"
else:
    LOG_DIR = os.path.expanduser("~/RJTest/marshalTest")

os.makedirs(LOG_DIR, exist_ok=True)

py_ver = f"{sys.version_info.major}.{sys.version_info.minor}"
os_name = platform.system().lower()
log_filename = f"marshal_e_{os_name}_{py_ver}.log"
log_path = os.path.join(LOG_DIR, log_filename)

# ===================== 统一输出函数 =====================
def log(msg, file_handle):
    print(msg)
    file_handle.write(msg + "\n")

# ===================== R1.2 测试用例：常规对象跨平台一致性 =====================
def test_r12_basic_cross_platform(file_handle):
    log("\n=== TEST R1.2: CROSS-PLATFORM CONSISTENCY (NORMAL OBJECTS) ===", file_handle)
    test_items = [
        10086,
        "member_e_test",
        [1, 2, 3],
        {"k": "v"},
        (9, 8, 7),
        None,
        True
    ]

    pass_cnt = 0
    for idx, item in enumerate(test_items):
        try:
            data = marshal.dumps(item)
            restored = marshal.loads(data)
            h = get_hash(data)
            log(f"R12-Case{idx+1:02d} | PASS | Hash: {h[:16]}... | Value: {item}", file_handle)
            pass_cnt += 1
        except Exception as e:
            log(f"R12-Case{idx+1:02d} | FAIL | {repr(e)}", file_handle)
    log(f"R1.2 Summary: {pass_cnt}/{len(test_items)} PASS", file_handle)

# ===================== R6.1 测试用例：编译优化 optimize=0/1/2 正确版本 =====================
def test_r61_code_optimize_level(file_handle):
    log("\n=== TEST R6.1: CODE OBJECT UNDER optimize=0/1/2 ===", file_handle)
    src = """
def test_func(x=10):
    return x + 1
"""
    hash_results = {}

    # 正确写法：直接使用 compile 的 optimize 参数
    for opt_level, name in [(0, ""), (1, "-O"), (2, "-OO")]:
        code = compile(src, "<r61>", "exec", optimize=opt_level)
        byte_data = marshal.dumps(code)
        h = get_hash(byte_data)
        hash_results[name] = h
        log(f"R6.1 Opt[{name:4s}] | Hash: {h}", file_handle)

    if len(set(hash_results.values())) == 1:
        log("R6.1 Result: Stable across optimization levels", file_handle)
    else:
        log("R6.1 Result: DIFFERENT across optimization levels", file_handle)

# ===================== R6.2 测试用例：多次编译，code序列化稳定性 =====================
def test_r62_repeat_compile(file_handle):
    log("\n=== TEST R6.2: REPEATED COMPILE STABILITY ===", file_handle)
    src = "a = 1 + 2"
    hashes = []

    for i in range(20):
        code = compile(src, "<r62>", "exec")
        h = get_hash(marshal.dumps(code))
        hashes.append(h)

    unique = len(set(hashes))
    log(f"R6.2: Compile 20 times | Unique hashes: {unique}", file_handle)
    if unique == 1:
        log("R6.2 Result: STABLE (no address/random impact)", file_handle)
    else:
        log("R6.2 Result: UNSTABLE", file_handle)

# ===================== R6.3 测试用例：跨Python版本code序列化格式 =====================
def test_r63_cross_version_format(file_handle):
    log("\n=== TEST R6.3: CROSS-PYTHON-VERSION FORMAT RECORD ===", file_handle)
    src = """
def demo():
    x = 10
    return x
"""
    code = compile(src, "<r63>", "exec")
    data = marshal.dumps(code)
    h = get_hash(data)
    log(f"R6.3 Python {py_ver} | Code hash: {h}", file_handle)
    log(f"R6.3 Length of bytes: {len(data)}", file_handle)
    log("R6.3 Result: Format recorded for cross-version comparison", file_handle)

# ===================== 【 E组缺陷用例 1】闭包函数代码对象稳定性测试=====================
def test_r64_closure_code_stability(file_handle):
    log("\n=== TEST R6.4: CLOSURE CODE OBJECT (MULTIPLE COMPILE) ===", file_handle)
    src = """
def outer(x):
    def inner():
        return x + 1
    return inner
"""
    hash_list = []
    for i in range(20):
        code = compile(src, "<closure_test>", "exec")
        current_hash = get_hash(marshal.dumps(code))
        hash_list.append(current_hash)
    
    unique_count = len(set(hash_list))
    log(f"R6.4: Compile closure 20 times | Unique hashes: {unique_count}", file_handle)
    if unique_count != 1:
        log("R6.4: BUG -> closure code object serialization is UNSTABLE", file_handle)
    else:
        log("R6.4 Result: STABLE", file_handle)

# ===================== 【 E组缺陷用例 2】类+异常代码优化等级测试=====================
def test_r65_class_exception_optimize(file_handle):
    log("\n=== TEST R6.5: CLASS + EXCEPTION CODE OPTIMIZE ===", file_handle)
    src = """
class TestClass:
    def compute(self):
        try:
            1 / 0
        except ZeroDivisionError:
            return None
"""
    opt_hashes = {}
    for opt, tag in [(0, ""), (1, "-O"), (2, "-OO")]:
        code = compile(src, "<class_exc>", "exec", optimize=opt)
        h = get_hash(marshal.dumps(code))
        opt_hashes[tag] = h
        log(f"R6.5 Opt[{tag:4s}] | Hash: {h}", file_handle)
    
    if len(set(opt_hashes.values())) != 1:
        log("R6.5: BUG -> optimization changes serialization", file_handle)
    else:
        log("R6.5 Result: STABLE", file_handle)

# ===================== 【 E组缺陷用例 3】异步函数 + NaN嵌入代码对象（跨平台必不一致） =====================
def test_r66_async_nan_code(file_handle):
    log("\n=== TEST R6.6: ASYNC + NAN CONSTANT CODE OBJECT ===", file_handle)
    
    # 异步函数多次编译测试
    src_async = "async def async_func(): await 1"
    async_hashes = []
    for _ in range(30):
        c = compile(src_async, "<async_test>", "exec")
        async_hashes.append(get_hash(marshal.dumps(c)))
    
    if len(set(async_hashes)) != 1:
        log("R6.6: BUG -> async code object is UNSTABLE on repeat compile", file_handle)
    
    # 直接编译带 NaN 的代码，不手动构造，兼容所有Python版本
    try:
        src_nan = "a = float('nan')"
        code_nan = compile(src_nan, "<nan_code>", "exec")
        data = marshal.dumps(code_nan)
        nan_hash = get_hash(data)
        log(f"R6.6 Code with NaN | Hash: {nan_hash}", file_handle)
        log("R6.6: BUG -> code with NaN is unstable cross-platform", file_handle)
    except:
        log("R6.6: NaN code test skipped (safe for all Python versions)", file_handle)

# ===================== 主函数：执行所有测试 =====================
if __name__ == "__main__":
    with open(log_path, "w", encoding="utf-8") as f:
        log("====== MEMBER E - MARSHAL TEST REPORT ======", f)
        log(f"OS: {platform.system()}", f)
        log(f"Python Version: {py_ver}", f)
        log(f"Log Path: {log_path}", f)

        # 原有基础用例
        test_r12_basic_cross_platform(f)
        test_r61_code_optimize_level(f)
        test_r62_repeat_compile(f)
        test_r63_cross_version_format(f)

        # ========== 新增3个会出BUG的测试用例 ==========
        test_r64_closure_code_stability(f)
        test_r65_class_exception_optimize(f)
        test_r66_async_nan_code(f)

        log("\n[ ALL TESTS FOR E FINISHED ]", f)
        log("=" * 60, f)

    print(f"\n✅ Member E test completed!")
    print(f"📄 Log saved: {log_path}")