-- 코드를 작성해주세요
select count(id) as fish_count, month(time) as MONTH
from fish_info
group by MONTH
order by month
;