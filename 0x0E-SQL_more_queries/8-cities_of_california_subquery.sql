-- Write a script that lists all the cities of California that can be found in
-- the database hbtn_0d_usa.
-- first we select the id and the name in the cities in which thier ids match
-- the id of California state, we don't know the id of it
SELECT id, `name` FROM cities
       WHERE id = (
       	     -- so here we select the id from states table in wich
	     -- its name match Calfornia
       	     SELECT id FROM states
	     	    WHERE `name` = "California"
		    )
       ORDER BY id ASC; -- and then they get sorted by the city id
