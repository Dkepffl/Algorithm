SELECT A.ITEM_ID,ITEM_NAME
FROM ITEM_INFO A JOIN ITEM_TREE B USING(ITEM_ID)
WHERE B.PARENT_ITEM_ID IS NULL
ORDER BY A.ITEM_ID ASC