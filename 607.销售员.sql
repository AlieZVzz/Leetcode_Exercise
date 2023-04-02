--
-- @lc app=leetcode.cn id=607 lang=mysql
--
-- [607] 销售员
--

-- @lc code=start
# Write your MySQL query statement below
select name from SalesPerson where sales_id not in (select sales_id from Orders left join Company on Company.com_id = Orders.com_id where Company.name='RED')
-- @lc code=end

