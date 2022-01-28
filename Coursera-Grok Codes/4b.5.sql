alter table star
add column ra float,
add column decl float;

delete from star;

copy star (kepler_id, t_eff, radius, ra, decl) from 'stars_full.csv' csv;
