SELECT D.DEPT_ID, D.DEPT_NAME_EN, ROUND(AVG(E.SAL),0) AS AVG_SAL
FROM HR_DEPARTMENT D JOIN HR_EMPLOYEES E USING(DEPT_ID)
GROUP BY D.DEPT_ID
ORDER BY AVG_SAL DESC