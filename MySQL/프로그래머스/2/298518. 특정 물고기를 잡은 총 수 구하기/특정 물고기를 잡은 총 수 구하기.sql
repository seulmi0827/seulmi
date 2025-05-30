-- 코드를 작성해주세요
select count(*) as fish_count
from fish_info A
inner join fish_name_info B
on A.fish_type = B.fish_type
where B.fish_name = 'BASS' or B.fish_name = 'SNAPPER'