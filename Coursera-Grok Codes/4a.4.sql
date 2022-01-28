select round(avg(p.t_eq),1),min(s.t_eff),max(s.t_eff)
from star s join planet p using (kepler_id)
where s.t_eff>(select avg(st.t_eff) from star st);
