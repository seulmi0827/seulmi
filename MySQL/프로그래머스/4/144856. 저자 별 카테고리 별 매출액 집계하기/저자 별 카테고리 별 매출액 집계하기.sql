-- 코드를 입력하세요
select c.author_id, c.author_name, c.category, sum(c.price*bs.sales) as total_sales
from (SELECT a.author_id, a.author_name, b.category, b.book_id, b.price
    from author as a
    inner join book as b
    on a.author_id = b.author_id) as c
inner join (select * from book_sales where SALES_DATE like '2022-01%') as bs
on c.book_id = bs.book_id
group by c.author_name, c.category 
order by c.author_id asc ,c.category desc