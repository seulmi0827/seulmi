-- 코드를 입력하세요
SELECT B.user_id, B.nickname, sum(A.price) as total_sales from used_goods_board A
INNER JOIN used_goods_user B
on A.writer_id = B.user_id
where A.status = 'done'
group by B.user_id
having total_sales >= 700000
order by total_sales asc
;