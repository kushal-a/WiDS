select s.radius as sun_radius,p.radius as planet_radius
from star as s , planet as p
where 
p.kepler_id = s.kepler_id and
s.radius/p.radius>1
order by sun_radius desc;
