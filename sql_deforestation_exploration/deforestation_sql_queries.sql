--- INITIALIZATION ---

DROP VIEW IF EXISTS forestation;


CREATE VIEW forestation AS
  (SELECT forest_area.country_code,
          forest_area.year,
          forest_area.forest_area_sqkm,
          land_area.country_name,
          land_area.total_area_sq_mi,
          regions.region,
          regions.income_group,
          forest_area.forest_area_sqkm / (land_area.total_area_sq_mi * 2.59) * 100 forest_percentage,
          land_area.total_area_sq_mi * 2.59 total_area_sqkm
   FROM forest_area
   JOIN land_area ON land_area.country_code = forest_area.country_code
   AND land_area.year = forest_area.year
   JOIN regions ON forest_area.country_code = regions.country_code);
   
   
   
--- GLOBAL SITUATION ---
--- creating subqueries for both years, the difference in sqkm and in percent, to get one result for all four parameters for the first paragraph ---
WITH a1990 AS
  (SELECT f.forest_area_sqkm AS world_1990_sqkm,
          f.year
   FROM forestation f
   WHERE f.country_name = 'World'
     AND f.year = 1990),
     a2016 AS
  (SELECT f.forest_area_sqkm AS world_2016_sqkm,
          f.year
   FROM forestation f
   WHERE f.country_name = 'World'
     AND f.year = 2016),
     diffs AS
  (SELECT world_1990_sqkm,
          world_2016_sqkm,
          world_2016_sqkm - world_1990_sqkm diff_sqkm,
          (world_2016_sqkm - world_1990_sqkm) / world_1990_sqkm * 100 AS diff_percent
   FROM a2016,
        a1990)
SELECT world_1990_sqkm,
       world_2016_sqkm,
       diff_sqkm,
       Round(diff_percent :: NUMERIC, 2) AS diff_percent
FROM diffs;



--- The query for the second paragraph. The values 1270000 and 1350000 are picked as ranges from the difference of -1324449 between 1990 and 2016 ---
SELECT DISTINCT f.country_name,
                Round(f.total_area_sqkm :: NUMERIC, 2) AS peru_sqkm
FROM forestation f
WHERE f.total_area_sqkm BETWEEN 1270000 AND 1350000;



--- REGIONAL OUTLOOK ---
--- This query outputs the regions and designated forests in 1990 and 2016, ordered by the highest difference in forestation between 1990 and 2016. All the data to fill in the table and extract the requested parameters are accessible ---
WITH r1990 AS
  (SELECT f.region,
          Round((SUM(f.forest_area_sqkm) * 100 / SUM(f.total_area_sqkm)) :: NUMERIC, 2) AS forest_percent_1990
   FROM forestation f
   WHERE f.year = 1990
   GROUP BY f.region),
     r2016 AS
  (SELECT f.region,
          Round((SUM(f.forest_area_sqkm) * 100 / SUM(f.total_area_sqkm)) :: NUMERIC, 2) AS forest_percent_2016
   FROM forestation f
   WHERE f.year = 2016
   GROUP BY f.region)
SELECT r1990.region,
       r1990.forest_percent_1990,
       r2016.forest_percent_2016,
       (r2016.forest_percent_2016 - r1990.forest_percent_1990) AS diff_percent
FROM r1990
JOIN r2016 ON r1990.region = r2016.region 
--- AND r1990.region = 'World'
--- NOTE: I uncomment the line above to reply to the first question regarding global development. to get all data, I comment it out ---
ORDER BY diff_percent ASC;



--- COUNTRY-LEVEL SUCCESS STORIES AND LARGEST CONCERNS ---
--- This query outputs the countries and region ordered by the highest increase of forests, in order to find out the largest concerns please look at the note below
---
WITH c1990 AS
  (SELECT f.country_name,
          f.region,
          Round(f.forest_area_sqkm :: NUMERIC, 2) AS forest_sqkm_1990
   FROM forestation f
   WHERE f.year = 1990),
     c2016 AS
  (SELECT f.country_name,
          Round(f.forest_area_sqkm :: NUMERIC, 2) AS forest_sqkm_2016
   FROM forestation f
   WHERE f.year = 2016)
SELECT c1990.country_name,
       c1990.region,
       c1990.forest_sqkm_1990,
       c2016.forest_sqkm_2016,
       (c2016.forest_sqkm_2016 - c1990.forest_sqkm_1990) AS forest_change_sqkm
FROM c1990
JOIN c2016 ON c1990.country_name = c2016.country_name
WHERE c1990.forest_sqkm_1990 IS NOT NULL
  AND c2016.forest_sqkm_2016 IS NOT NULL
  AND c1990.country_name != 'World' 
  ---ORDER BY forest_change_sqkm;
--- NOTE: by using the line above the results will be shown in ascending order, which means they order the country and region with the highest decrease of forest first ---
ORDER BY forest_change_sqkm DESC;