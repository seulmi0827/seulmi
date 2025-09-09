-- 코드를 입력하세요
select title, board_id, reply_id, writer_id, contents, date_format(created_date,'%Y-%m-%d') from 
(SELECT 
    board.title,
    board.board_id,  
    reply.reply_id, 
    reply.writer_id, 
    reply.contents, 
    reply.created_date
from used_goods_board as board
join used_goods_reply as reply
on board.board_id =  reply.board_id
where board.created_date like '2022-10%'
order by created_date, title) as m