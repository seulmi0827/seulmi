-- 코드를 입력하세요
SELECT A.book_id, B.author_name, left(A.published_date,10) from book as A
left join author as B
on A.author_id = B.author_id
where A.category like '경제'
order by A.published_date

;