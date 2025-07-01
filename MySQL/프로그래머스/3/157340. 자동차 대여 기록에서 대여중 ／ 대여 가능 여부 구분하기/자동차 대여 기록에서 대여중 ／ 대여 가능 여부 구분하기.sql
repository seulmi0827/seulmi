-- 코드를 입력하세요
select origin.car_id , coalesce(finder.availability,'대여 가능')
from (select distinct(car_id) from car_rental_company_rental_history)
as origin
left join (select car_id ,'대여중' as availability
from car_rental_company_rental_history 
where start_date <= '2022-10-16' and end_date >='2022-10-16'
group by car_id) as finder
on origin.car_id = finder.car_id
order by car_id desc