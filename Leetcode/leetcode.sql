-- Leetcode MySQL

-- https://leetcode.com/JHarrisJoshua/

---------------------- 534. Game Play Analysis III -----------------------------
SELECT   player_id
        ,event_date
        ,SUM(games_played)
            OVER (
            PARTITION BY player_id
            ORDER BY event_date
            ROWS BETWEEN UNBOUNDED PRECEDING
                 AND CURRENT ROW
            ) AS games_played_so_far
FROM Activity


---------------------- 585. Investments in 2016 --------------------------------
WITH CTE AS (
  SELECT    *
            , COUNT(*) OVER (PARTITION BY tiv_2015) AS count_2015
            , COUNT(*) OVER (PARTITION BY lat, lon) AS count_loc
  FROM Insurance
)

SELECT ROUND(SUM(tiv_2016), 2) as tiv_2016
FROM CTE
WHERE count_2015 > 1 AND count_loc = 1


------------ 1378. Replace Employee ID With The Unique Identifier --------------
SELECT unique_id, name FROM Employees e
LEFT JOIN EmployeeUNI u USING(id)


------------------ 596. Classes More Than 5 Students ---------------------------
SELECT  class
FROM Courses
GROUP BY class
HAVING COUNT(*) >= 5

