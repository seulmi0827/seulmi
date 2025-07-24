-- 코드를 입력하세요
select cart_id
from 
    (SELECT cart_id, name from cart_products
    where name in ('Yogurt','Milk')
    group by cart_id, name) as filtered
group by cart_id
having count(name) >1
