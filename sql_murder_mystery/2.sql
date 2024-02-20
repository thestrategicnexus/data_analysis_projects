-- Select all columns from the person table and alias it as 'p'
-- Join the person table with the interview table 
SELECT *
FROM person as p 
Inner Join interview as i 
ON p.id = i.person_id
WHERE (p.name LIKE "Annabel%" AND p.address_street_name = "Franklin Ave") 
OR (p.address_street_name = "Northwestern Dr" AND p.address_number = (SELECT MAX(p2.address_number) 
FROM person as p2 WHERE p2.address_street_name ="Northwestern Dr" )) ;

