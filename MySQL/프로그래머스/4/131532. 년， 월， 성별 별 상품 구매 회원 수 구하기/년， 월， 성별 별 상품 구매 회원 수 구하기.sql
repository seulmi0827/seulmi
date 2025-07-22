SELECT  
    date_format(os.SALES_DATE, '%Y') as year, 
    date_format(os.SALES_DATE, '%m') as month, 
    ui.gender as gender,
    count(distinct(os.user_id)) as users
from user_info as ui
join online_sale as os
on ui.user_id = os.user_id
where ui.gender is not null
group by year, month, gender
order by year, month, gender