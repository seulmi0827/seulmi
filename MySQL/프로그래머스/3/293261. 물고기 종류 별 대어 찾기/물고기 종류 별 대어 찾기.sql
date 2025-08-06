-- 코드를 작성해주세요
select id_in.id , origin.fish_name, id_in.length
from (select  n.fish_name as fish_name, max(i.length) as length from fish_info as i
join fish_name_info as n
on i.fish_type = n.fish_type
group by n.fish_name) as origin
join (select A.id, A.length as length ,B.fish_name as fish_name
from fish_info as A
join fish_name_info as B
on A.fish_type = B.fish_type) as id_in
on origin.fish_name = id_in.fish_name and origin.length = id_in.length
order by id