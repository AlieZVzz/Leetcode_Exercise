--
-- @lc app=leetcode.cn id=183 lang=mysql
--
-- [183] 从不订购的客户
--

-- @lc code=start
# Write your MySQL query statement below
select name  Customers  from Customers c left join Orders o  on c.Id = o.CustomerId  where o.CustomerId is null;
-- @lc code=end

