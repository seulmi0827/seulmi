select case 
            when q<=1 then '1Q'
            when q>1 and q<=2 then '2Q'
            when q>2 and q<=3 then '3Q'
            else '4Q'
            end as quarter, 
        count(*) as ecoli_count
from (select id, date_format(differentiation_date,'%m')/3 as q
        from ecoli_data) as q_tb 
group by quarter
order by quarter