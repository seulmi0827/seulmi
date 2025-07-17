-- 코드를 입력하세요
SELECT history_id,
        car_id,
        DATE_FORMAT(START_DATE, '%Y-%m-%d'),
        DATE_FORMAT(end_DATE, '%Y-%m-%d'),
        case when datediff(end_date, start_date) >=29 then '장기 대여'
                else '단기 대여'
                end as RENT_TYPE
from car_rental_company_rental_history
where start_date like '2022-09%'
order by history_id desc 
;