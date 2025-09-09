-- 코드를 작성해주세요
select emp.emp_no, emp.emp_name,s.grade,s.percent*emp.sal as bonus
from hr_employees as emp
join (select emp_no,score ,case
                when score >=96 then 'S'
                when 96>score and score >=90 then 'A'
                when 90>score and score >=80 then 'B'
                else 'C' 
                end as grade,
            case
                when score >=96 then 0.2
                when 96>score and score >=90 then 0.15
                when 90>score and score >=80 then 0.1
                else 0
                end as percent
    from (select emp_no, avg(score) as score from hr_grade group by emp_no) as score_tb) as s
on s.emp_no = emp.emp_no