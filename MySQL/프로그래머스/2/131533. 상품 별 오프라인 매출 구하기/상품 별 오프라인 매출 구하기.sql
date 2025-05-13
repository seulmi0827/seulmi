-- 코드를 입력하세요
SELECT A.product_code, sum(A.price*B.sales_amount) as sales from product A
left join offline_sale B
on A.product_id = B.product_id
group by A.product_code
order by sales desc, A.product_code asc
;