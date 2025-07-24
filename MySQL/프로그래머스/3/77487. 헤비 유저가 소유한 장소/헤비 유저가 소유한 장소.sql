select pl.* from places as pl
join (SELECT host_id
        from places
        group by host_id
        having count(id) > 1) as filtered
on pl.host_id = filtered.host_id