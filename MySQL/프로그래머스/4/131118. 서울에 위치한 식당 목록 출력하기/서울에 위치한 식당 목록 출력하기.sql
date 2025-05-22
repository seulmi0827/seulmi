-- 코드를 입력하세요
SELECT A.rest_id, A.rest_name, A.food_type, A.favorites, A.address, B.score
from rest_info A
inner join (select rest_id, round(avg(REVIEW_SCORE),2) as score 
            from rest_review
            group by rest_id) B
on A.rest_id = B.rest_id
where A.address like '서울%'
order by score desc, favorites desc
;