update planet 
set kepler_name = null
where status!=upper('confirmed');

delete from planet where radius<0;
