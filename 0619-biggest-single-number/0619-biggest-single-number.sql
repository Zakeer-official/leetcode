SELECT COALESCE(MAX(num), NULL) AS num
FROM (
    SELECT num
    FROM MyNumbers
    GROUP BY num
    HAVING COUNT(*) = 1
) atable;
