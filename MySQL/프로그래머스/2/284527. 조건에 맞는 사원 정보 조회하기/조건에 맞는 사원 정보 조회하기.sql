-- 코드를 작성해주세요
select B.score, A.emp_no, A.emp_name, A.position, A.email from hr_employees A
inner join (select emp_no, sum(score) as score from hr_grade
where year = 2022
group by emp_no
order by score desc
limit 1) B
on B.emp_no = A.emp_no
;