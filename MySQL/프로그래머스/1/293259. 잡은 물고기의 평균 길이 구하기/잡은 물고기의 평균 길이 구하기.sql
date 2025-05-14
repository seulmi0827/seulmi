-- 코드를 작성해주세요
select round(sum(coalesce(length,10))/count(id),2) as average_length from fish_info
;

