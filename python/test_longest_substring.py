import pytest
import sys
import os

test_dir = os.path.dirname(os.path.abspath(__file__))
if test_dir not in sys.path:
    sys.path.append(test_dir)

from longest_substring import Solution  

@pytest.fixture(scope="function")  
def solution():
    return Solution()

test_cases = [
    # 常规场景（4个）
    ("abcdef", 6, "无重复字符（全唯一）：set持续add，无remove"),
    ("abcabcbb", 3, "部分重复（中间重复）：重复时remove左侧字符，窗口重置"),
    ("bbbbb", 1, "连续重复（末尾重复）：每次right移动都触发remove"),
    ("pwwkew", 3, "重复字符间隔出现：窗口从'pw'→'wke'"),
    # 边界条件（4个）
    ("", 0, "空字符串：set初始为空，无循环执行"),
    ("a", 1, "单字符字符串：仅一次add，窗口长度1"),
    ("aa", 1, "双字符重复：第二次循环触发remove，窗口重置为1"),
    ("ab", 2, "双字符不重复：无remove，窗口长度递增至2"),
    # 特殊场景（4个）
    ("a b c", 3, "包含空格字符：空格作为独立字符，set正常判重"),
    ("a1b2!c", 6, "包含数字和符号：混合字符无重复，返回全长"),
    ("abcde"*200 + "fghij", 10, "长字符串（1005字符）：每5个重复，最长子串10"),
    ("dvdf", 3, "重复字符在窗口中间：窗口从'dv'→'vdf'")
]

@pytest.mark.parametrize("s, expected, case_desc", test_cases)
def test_length_of_longest_substring(solution, s, expected, case_desc):
    """
    测试lengthOfLongestSubstring函数的全场景功能
    :param solution: Fixture提供的Solution实例
    :param s: 输入字符串
    :param expected: 预期最长子串长度
    :param case_desc: 测试场景描述（用于失败时定位问题）
    """

    try: 
        decoded_desc = codecs.decode(case_desc, 'unicode-escape')
    except Exception as e:
        decoded_desc = case_desc
        print(f"中文解码警告：{e}，将使用原始描述：{case_desc}")

    result = solution.lengthOfLongestSubstring(s)
    # 断言结果是否符合预期（失败时显示场景描述）
    assert result == expected, \
        f"测试失败：{decoded_desc}\n输入s：{s[:20]}...（总长{len(s)}）\n预期结果：{expected}\n实际结果：{result}"

    print(f"✓ 用例通过：{decoded_desc}（输入长度：{len(s)}）")
