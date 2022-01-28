select p.koi_name,p.radius,st.radius
from (select radius,kepler_id from star order by radius desc limit 5) st
join planet p using (kepler_id);
