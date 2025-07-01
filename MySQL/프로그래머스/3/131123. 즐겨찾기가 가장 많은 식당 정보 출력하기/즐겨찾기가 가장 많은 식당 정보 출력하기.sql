-- 코드를 입력하세요
select B.food_type, B.rest_id, B.rest_name, B.favorites
from (select max(favorites) as favorites, food_type from rest_info 
group by food_type) as A
left join rest_info as B
on A.favorites = B.favorites and A.food_type = B.food_type
order by B.food_type desc