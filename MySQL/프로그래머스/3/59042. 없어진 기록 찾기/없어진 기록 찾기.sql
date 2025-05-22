-- 코드를 입력하세요
select animal_id, name from animal_outs
where animal_id not in (SELECT B.animal_id
                        from animal_outs B
                        inner join animal_ins A
                        on A.animal_id = B.animal_id)
order by animal_id
;
