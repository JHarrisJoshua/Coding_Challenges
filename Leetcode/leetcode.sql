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


------------------ 596. Classes More Than 5 Students ---------------------------
SELECT  class
FROM Courses
GROUP BY class
HAVING COUNT(*) >= 5


--------------------- 601. Human Traffic of Stadium ----------------------------
WITH CTE1 AS (
        SELECT  *
                , id - RANK() OVER (ORDER BY id) as rnk
        FROM Stadium
        WHERE people >= 100
), CTE2 AS (
        SELECT  *
                , COUNT(*) OVER (PARTITION BY rnk) cnt
        FROM CTE1
)
SELECT id, visit_date, people FROM CTE2
WHERE cnt >= 3
ORDER BY visit_date


------------------ 1350. Students With Invalid Departments ---------------------
SELECT s.id, s.name FROM Students s
LEFT JOIN Departments d on s.department_id=d.id
WHERE ISNULL(d.id)


------------ 1378. Replace Employee ID With The Unique Identifier --------------
SELECT unique_id, name FROM Employees e
LEFT JOIN EmployeeUNI u USING(id)


--------------------- 1479. Sales by Day of the Week ---------------------------
SELECT
    item_category as CATEGORY
    , SUM(IF(DAYNAME(order_date)='Monday', quantity, 0)) as 'MONDAY'
    , SUM(IF(DAYNAME(order_date)='Tuesday', quantity, 0)) as 'TUESDAY'
    , SUM(IF(DAYNAME(order_date)='Wednesday', quantity, 0)) as 'WEDNESDAY'
    , SUM(IF(DAYNAME(order_date)='Thursday', quantity, 0)) as 'THURSDAY'
    , SUM(IF(DAYNAME(order_date)='Friday', quantity, 0)) as 'FRIDAY'
    , SUM(IF(DAYNAME(order_date)='Saturday', quantity, 0)) as 'SATURDAY'
    , SUM(IF(DAYNAME(order_date)='Sunday', quantity, 0)) as 'SUNDAY'
FROM Items
LEFT JOIN Orders USING(item_id)
GROUP BY CATEGORY
ORDER BY CATEGORY


--------------------------- 1683. Invalid Tweets -------------------------------
SELECT  tweet_id
FROM Tweets
WHERE length(content) > 15


---------- 1821. Find Customers With Positive Revenue this Year ----------------
SELECT customer_id FROM Customers
WHERE year = 2021 and revenue > 0


------------------------ 1934. Confirmation Rate -------------------------------
SELECT  user_id
        , ROUND(SUM(IF(action="Confirmed", 1,0))
          /  COUNT(*), 2) as confirmation_rate
FROM Signups s
LEFT JOIN Confirmations c USING(user_id)
GROUP BY user_id


------------- 1978. Employees Whose Manager Left the Company -------------------
SELECT  employee_id
FROM Employees
WHERE
  manager_id NOT IN (SELECT employee_id FROM Employees)
  AND
  salary < 30000
ORDER BY employee_id

------------- 2026. Low-Quality Problems --------------------------------------
SELECT problem_id FROM Problems
WHERE (likes/(likes+dislikes)) < .6
ORDER BY problem_id
