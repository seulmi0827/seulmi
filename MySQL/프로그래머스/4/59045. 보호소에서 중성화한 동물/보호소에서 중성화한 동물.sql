-- 코드를 입력하세요
SELECT A.animal_id, A.animal_type, A.name from animal_ins A
INNER JOIN animal_outs B
on A.animal_id = B.animal_id
where A.sex_upon_intake like 'intact%' 
    and (B.sex_upon_outcome like 'spayed%' or B.sex_upon_outcome like 'Neutered%')
order by A.animal_id
;