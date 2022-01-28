create table star (
    kepler_id integer primary key,
    t_eff integer not null,
    radius float not null
    );

create table planet (
    kepler_id integer references star (kepler_id),
    koi_name varchar(20) primary key,
    kepler_name varchar(20),
    status varchar(20) not null,
    period float,
    radius float,
    t_eq integer
    );

copy star (kepler_id,t_eff,radius) from 'stars.csv' CSV;
copy planet (kepler_id,koi_name,kepler_name,status,period,radius,t_eq) from 'planets.csv' csv;
