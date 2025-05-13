-- 코드를 입력하세요
SELECT A.category, sum(B.sales) from book A
left join book_sales B
on A.book_id = B.book_id
where B.sales_date >= '2022-01-01' and B.sales_date < '2022-02-01'
group by A.category
order by category
;