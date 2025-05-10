-- 코드를 입력하세요
SELECT 
    mcdp_cd as 진료과코드 ,
    count(apnt_no) as 5월예약건수
from 
    appointment
where 
    Month(apnt_ymd) = 5 and
    Year(apnt_ymd) = 2022
group by 
    mcdp_cd
order by 5월예약건수, 진료과코드
;