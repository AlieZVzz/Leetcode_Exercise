--
-- @lc app=leetcode.cn id=1965 lang=mysql
--
-- [1965] 丢失信息的雇员
--

-- @lc code=start
# Write your MySQL query statement below
select employee_id from (select a.employee_id from Employees a left join Salaries b on a.employee_id = b.employee_id where b.salary is null union select b.employee_id  from Employees a right join Salaries b on a.employee_id = b.employee_id where a.name is null ) o order by o.employee_id asc
-- @lc code=end

