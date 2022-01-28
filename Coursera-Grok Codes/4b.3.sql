create table planet (
    kepler_id integer not null,
    koi_name varchar(15) not null unique,
    kepler_name varchar(15) ,
    status varchar(20) not null,
    radius float not null
    );
    
insert into planet (kepler_id,koi_name,kepler_name,status,radius) values
(6862328,	'K00865.01',	null,	        'CANDIDATE',	119.021),
(10187017,	'K00082.05',	'Kepler-102 b',	'CONFIRMED',	5.286),
(10187017,	'K00082.04',	'Kepler-102 c',	'CONFIRMED',	7.071);
