-- Lists all the cities of California that can be found in the database
SELECT cities.id, cities.name FROM states, cities
WHERE cities.state_id = states.id AND statws.name = "California";
