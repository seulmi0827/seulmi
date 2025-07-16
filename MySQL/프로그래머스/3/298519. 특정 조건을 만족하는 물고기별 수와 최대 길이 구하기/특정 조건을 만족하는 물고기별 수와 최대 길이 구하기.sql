-- 코드를 작성해주세요
select fish_count, max_length, fish_type
from (select count(id)as fish_count,
    fish_type, 
    avg(coalesce(length,10)) as avg_len,
    max(length) as max_length
from fish_info
group by fish_type) as my_tb
where avg_len >=33
order by fish_type
