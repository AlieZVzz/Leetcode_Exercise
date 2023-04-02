--
-- @lc app=leetcode.cn id=197 lang=mysql
--
-- [197] 上升的温度
--

-- @lc code=start
# Write your MySQL query statement below
select w1.id id
from weather w1
where w1.temperature > (
    select w2.temperature
    from weather w2
    where datediff(w1.recordDate, w2.recordDate) = 1
)
-- @lc code=end

