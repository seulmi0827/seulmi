-- 코드를 입력하세요
SELECT order_id, product_id, left(out_date,10),'출고완료' as 출고여부 from food_order
where out_date <= '2022-05-01'
union
SELECT order_id, product_id, left(out_date,10),'출고대기' from food_order
where out_date > '2022-05-01'
union
SELECT order_id, product_id, left(out_date,10),'출고미정' from food_order
where out_date is null
order by order_id
;