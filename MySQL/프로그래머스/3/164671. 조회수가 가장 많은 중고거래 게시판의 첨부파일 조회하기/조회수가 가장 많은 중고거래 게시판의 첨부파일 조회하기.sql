-- 코드를 입력하세요
SELECT concat('/home/grep/src/',board_id,'/',file_id,file_name,file_ext) as file_path
from used_goods_file
where board_id like (select board_id
     from used_goods_board 
     order by VIEWS desc 
     limit 1)
order by file_id desc