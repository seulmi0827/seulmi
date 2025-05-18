-- 코드를 작성해주세요
select A.item_id, A.item_name
from item_info A
inner join item_tree B
on A.item_id = B.item_id
where B.parent_item_id is null
;