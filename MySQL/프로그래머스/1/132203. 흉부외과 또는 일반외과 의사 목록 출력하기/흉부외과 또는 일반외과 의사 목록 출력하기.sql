-- 코드를 입력하세요
SELECT dr_name, dr_id, mcdp_cd, left(hire_ymd,10) from doctor
where mcdp_cd like 'CS' or mcdp_cd like 'GS'
order by hire_ymd desc
;