--
-- @lc app=leetcode.cn id=176 lang=mysql
--
-- [176] 第二高的薪水
--

-- @lc code=start
# Write your MySQL query statement below
select(
    select
        salary
    from (
        select
            distinct(salary),
            dense_rank() over(order by salary desc) rk  -- 注意，这边必须用dense_rank，这样在有重复薪水值的时候可以避免跳过2
        from Employee
    ) a where rk = 2
) as SecondHighestSalary
-- @lc code=end

