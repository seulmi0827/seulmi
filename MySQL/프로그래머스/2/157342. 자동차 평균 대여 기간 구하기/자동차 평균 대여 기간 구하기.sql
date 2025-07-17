-- 코드를 입력하세요
select car_id, round(avg(diff),1) as AVERAGE_DURATION
from (SELECT car_id, DATEDIFF(end_date,start_date)+1 as diff
    from car_rental_company_rental_history) as diff_tb
group by car_id
having avg(diff) >=7
order by AVERAGE_DURATION desc, car_id desc
;