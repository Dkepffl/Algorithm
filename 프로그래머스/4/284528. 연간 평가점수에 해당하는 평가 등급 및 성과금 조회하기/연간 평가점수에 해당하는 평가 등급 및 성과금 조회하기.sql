WITH A AS (SELECT EMP_NO, AVG(SCORE) AS AVG_SCORE
           FROM HR_GRADE
           GROUP BY EMP_NO),
     B AS (SELECT EMP_NO, CASE WHEN AVG_SCORE >= 96 THEN 'S'
               WHEN AVG_SCORE >= 90 THEN 'A'
               WHEN AVG_SCORE >= 80 THEN 'B'
               ELSE 'C' END AS GRADE
           FROM A)

SELECT B.EMP_NO, E.EMP_NAME, B.GRADE,  CASE WHEN B.GRADE='S' THEN E.SAL*0.2
                                            WHEN B.GRADE='A' THEN E.SAL*0.15
                                            WHEN B.GRADE='B' THEN E.SAL*0.1
                                            ELSE 0 END AS BONUS
FROM B JOIN HR_EMPLOYEES E USING (EMP_NO)
ORDER BY B.EMP_NO