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


------------ 1378. Replace Employee ID With The Unique Identifier --------------
SELECT unique_id, name FROM Employees e
LEFT JOIN EmployeeUNI u USING(id)

