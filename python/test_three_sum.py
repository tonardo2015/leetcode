import sys
import os
import pytest
from typing import List

test_dir = os.path.dirname(os.path.abspath(__file__))
if test_dir not in sys.path:
    sys.path.append(test_dir)

from three_sum import Solution

class TestThreeSum:
    def setup_method(self):
        self.solution = Solution()

    @pytest.mark.parametrize("nums, expected", [
        # 常规测试用例1：包含多个有效组合
        ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]),
        # 常规测试用例2：无重复元素的有效组合
        ([-2, 0, 1, 1, 2], [[-2, 0, 2], [-2, 1, 1]]),
        # 边界情况1：空列表
        ([], []),
        # 边界情况2：元素数量不足3个
        ([0], []),
        ([1, 2], []),
        # 边界情况3：全为0的列表
        ([0, 0, 0, 0], [[0, 0, 0]]),
        # 重复元素测试1：连续重复的左/右指针元素
        ([-2, -2, 0, 0, 2, 2], [[-2, 0, 2]]),
        # 重复元素测试2：中间元素重复
        ([1, 1, 1, -2], [[-2, 1, 1]]),
        # 全为正数：无有效组合
        ([1, 2, 3, 4], []),
        # 全为负数：无有效组合
        ([-5, -4, -3], []),
        # 混合正负但无有效组合
        ([-1, 2, 3, 4], []),
        # 包含多个零的组合
        ([-3, 0, 1, 2, -1, 0, 3], [[-3, 1, 2], [-1, 0, 1], [-3, 0, 3]]), 
        # 较大数值范围测试
        ([-1000, -1000, 2000, 1000], [[-1000, -1000, 2000]]),  # 假设输入包含1000
    ])
    def test_three_sum(self, nums: List[int], expected: List[List[int]]):
        result = self.solution.three_sum(nums)
        
        # 排序结果中的每个子列表，确保比较时不受顺序影响
        # （因为题目要求三元组内部元素顺序无关，但整体列表顺序可能因实现略有差异）
        sorted_result = [sorted(triplet) for triplet in result]
        sorted_expected = [sorted(triplet) for triplet in expected]
        
        # 验证结果长度一致
        assert len(sorted_result) == len(sorted_expected), f"结果长度不符：预期{len(sorted_expected)}，实际{len(sorted_result)}"
        
        # 验证每个三元组都存在于预期结果中（不考虑整体顺序）
        for triplet in sorted_result:
            assert triplet in sorted_expected, f"意外的三元组：{triplet}"
