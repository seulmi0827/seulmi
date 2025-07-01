-- 코드를 입력하세요
select A.category, A.max_price, B.product_name from 
(SELECT category, max(price) as max_price
from food_product
where category in ('국','김치','과자','식용유')
group by category
order by price desc) as A
left join food_product as B
on A.category = B.category and A.max_price = B.price
;