#
# @lc app=leetcode.cn id=763 lang=python3
#
# [763] 划分字母区间
#

# @lc code=start
from typing import List
class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        dic = {s: index for index, s in enumerate(S)}   #存储某个字母对应地最后一个序号
        num = 0  #直接计数
        result = []
        j = dic[S[0]]  #第一个字符的最后位置

        for i in range(len(S)):  #逐个遍历
            num += 1  #找到一个就加1个长度
            if dic[S[i]] > j:  #思路一样，如果最后位置比刚才的大，就更新最后位置
                j = dic[S[i]]
            if i == j:  #思路一样，形式不同，这里就是找到这一段的结束了，就说明当前位置的index和这个字母在字典里的最后位置应该是相同的。
                result.append(num)  # 加入result
                num = 0 # 归0
        return result


# @lc code=end
