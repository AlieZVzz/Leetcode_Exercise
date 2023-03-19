--
-- @lc app=leetcode.cn id=1581 lang=mysql
--
-- [1581] 进店却未进行过交易的顾客
--

-- @lc code=start
# Write your MySQL query statement below
select a.customer_id, count(1) count_no_trans 
    from Visits a
    where a.visit_id not in (select b.visit_id from Transactions b)
    group by a.customer_id

-- @lc code=end

