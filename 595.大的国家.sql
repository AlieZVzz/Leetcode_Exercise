--
-- @lc app=leetcode.cn id=595 lang=mysql
--
-- [595] 大的国家
--

-- @lc code=start
# Write your MySQL query statement below
select name, population, area from World where area >=3e6 or population >= 25e6;
-- @lc code=end

