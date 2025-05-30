-- 코드를 입력하세요
SELECT board_id, writer_id, title, price, case
                                            when status = 'Done' then '거래완료'
                                            when status = 'reserved' then '예약중'
                                            else '판매중'
                                            end as status
from USED_GOODS_BOARD
where created_date = '2022-10-5'
order by board_id desc
;
