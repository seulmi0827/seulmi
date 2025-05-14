-- 코드를 입력하세요
SELECT distinct(A.car_id) from car_rental_company_car A
left join car_rental_company_rental_history B
on A.car_id = B.car_id
where month(B.start_date) = 10 and A.car_type = '세단'
order by A.car_id desc
;