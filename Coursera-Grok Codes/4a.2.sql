select s.radius , count(koi_name)
from star as s
join planet as p using (kepler_id)
where s.radius>1
group by kepler_id
having count(koi_name)>1
order by s.radius desc;
