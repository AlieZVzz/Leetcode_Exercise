--
-- @lc app=leetcode.cn id=608 lang=mysql
--
-- [608] 树节点
--

-- @lc code=start
# Write your MySQL query statement below
select o.id, case when o.p_id is null then 'Root' when o.c_id is null then 'Leaf' else 'Inner' end type from (
select a.id,a.p_id, b.c_id from tree a left join (select  p_id,group_concat(id) c_id from tree group by p_id) b on a.id = b.p_id) o;
-- @lc code=end

