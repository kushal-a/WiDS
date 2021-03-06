select s.kepler_id,s.t_eff,s.radius
from star s
left outer join planet p using (kepler_id)
where p.koi_name is null
order by s.t_eff desc;
