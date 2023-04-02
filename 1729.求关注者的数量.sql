--
-- @lc app=leetcode.cn id=1729 lang=mysql
--
-- [1729] 求关注者的数量
--

-- @lc code=start
# Write your MySQL query statement below
select user_id, count(DISTINCT follower_id) as followers_count from Followers GROUP by user_id;
-- @lc code=end

