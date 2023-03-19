--
-- @lc app=leetcode.cn id=1873 lang=mysql
--
-- [1873] 计算特殊奖金
--

-- @lc code=start
# Write your MySQL query statement below
select employee_id, case when name not like 'M%' and mod(employee_id, 2)=1 then salary else 0 end bonus from Employees order by employee_id asc;
-- @lc code=end

