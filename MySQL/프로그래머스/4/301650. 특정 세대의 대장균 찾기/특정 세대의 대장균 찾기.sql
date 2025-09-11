with 
    one_s as (select id 
              from ecoli_data 
              where parent_id is null),
    two_s as (select id 
              from ecoli_data 
              where parent_id in (select id 
                                  from one_s))
select id 
from ecoli_data 
where parent_id in (select id 
                    from two_s)