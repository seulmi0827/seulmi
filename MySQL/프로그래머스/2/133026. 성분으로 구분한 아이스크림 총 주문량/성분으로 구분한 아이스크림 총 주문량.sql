-- 코드를 입력하세요
SELECT B.ingredient_type, sum(A.total_order) TOTAL_ORDER
from first_half A
left join icecream_info B
on A.flavor = B.flavor
group by B.ingredient_type
order by TOTAL_ORDER

;