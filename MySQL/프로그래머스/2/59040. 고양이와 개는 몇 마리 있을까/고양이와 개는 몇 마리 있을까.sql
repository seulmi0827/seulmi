-- 코드를 입력하세요
SELECT animal_type, count(animal_id) from animal_ins
group by animal_type
order by case when animal_type ='Cat' then 1 when animal_type = 'Dog' then 2 end
;