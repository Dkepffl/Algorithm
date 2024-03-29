SELECT DATE_FORMAT(DATETIME, "%H") AS HOUR, COUNT(ANIMAL_ID)
FROM ANIMAL_OUTS
WHERE DATE_FORMAT(DATETIME, "%H") BETWEEN 9 and 19
GROUP BY DATE_FORMAT(DATETIME, "%H")
ORDER BY HOUR