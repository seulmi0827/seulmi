-- 코드를 작성해주세요
select origin.id, coalesce(tmp.cnt,0) as child_count
from ecoli_data as origin
left join (select parent_id, count(*) as cnt
            from ecoli_data
            where parent_id is not null
            group by parent_id) as tmp
on origin.id = tmp.parent_id
order by id