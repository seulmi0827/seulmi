-- 코드를 입력하세요
SELECT fh.flavor
from first_half as fh
join (select 
        flavor, 
        sum(total_order) as total_order2
      from july 
      group by flavor) as ju
on fh.flavor = ju.flavor
order by (total_order + total_order2) desc
limit 3