-- Select all columns from the crime_scene_report table
SELECT *
FROM crime_scene_report
-- Filter records
WHERE city = 'SQL City'
AND type = 'murder'
AND date = '20180115';