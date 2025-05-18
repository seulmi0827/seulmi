-- 코드를 작성해주세요
select A.dept_id, A.dept_name_en, round(avg(B.sal),0) as avg_sal
from hr_department A
inner join hr_employees B
on A.dept_id = B.dept_id
group by A.dept_id, A.dept_id
order by avg_sal desc
;