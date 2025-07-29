-- 코드를 입력하세요
select 
        cast(date_format(start_date,'%c') as signed) as month,
        car_id ,
        count(history_id) as records
from car_rental_company_rental_history
where car_id in (SELECT car_id
                from car_rental_company_rental_history
                where start_date >= "2022-08-01" and start_date < "2022-11-01"
                group by car_id
                having count(history_id) >=5)
    and start_date >= "2022-08-01" 
    and start_date < "2022-11-01"
group by car_id, month
having records > 0
order by month, car_id desc