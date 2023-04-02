--
-- @lc app=leetcode.cn id=1890 lang=mysql
--
-- [1890] 2020年最后一次登录
--

-- @lc code=start
# Write your MySQL query statement below
select user_id, max(time_stamp) as  last_stamp from Logins where year(time_stamp)=2020 group by user_id; 
-- @lc code=end

