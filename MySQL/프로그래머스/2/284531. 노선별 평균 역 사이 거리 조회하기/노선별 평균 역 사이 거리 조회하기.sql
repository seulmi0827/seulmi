select route,
    concat(t_dis,'km') as TOTAL_DISTANCE,
    concat(a_dis,'km') as AVERAGE_DISTANCE
from (select 
        route ,
        round(sum(d_between_dist),1) as t_dis, 
        round(avg(d_between_dist),2) as a_dis
    from subway_distance
    group by route
    order by t_dis desc) as revised_df