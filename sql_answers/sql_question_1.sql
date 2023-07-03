WITH CTE AS (SELECT ORDERS.ORDER_ID, SELLER_ID, EXTRACT(MONTH FROM ORDER_PURCHASE_TIMESTAMP) MONTH,
                    EXTRACT(WEEK FROM ORDER_PURCHASE_TIMESTAMP) WEEK,
                    EXTRACT(DAY FROM ORDER_PURCHASE_TIMESTAMP) DAY
                    FROM TAKE_HOME_CHALLENGE.ECOMMERCE.ORDERS ORDERS
                    LEFT JOIN TAKE_HOME_CHALLENGE.ECOMMERCE.ORDER_ITEMS ORDER_ITEMS
                    ON ORDERS.ORDER_ID=ORDER_ITEMS.ORDER_ID
                    WHERE EXTRACT(YEAR FROM ORDER_PURCHASE_TIMESTAMP)= 2017),                   
MONTHLY_TEMP AS (SELECT SELLER_ID, MONTH
FROM CTE
GROUP BY MONTH,SELLER_ID
HAVING COUNT(ORDER_ID)>=25
ORDER BY MONTH),
MONTHLY AS (SELECT COUNT(SELLER_ID) MONTHLY_ACTIVE_SELLER, MONTH
FROM MONTHLY_TEMP
GROUP BY MONTH),
WEEKLY_TEMP AS (SELECT COUNT(ORDER_ID),SELLER_ID, WEEK, MONTH
FROM CTE
GROUP BY WEEK, MONTH, SELLER_ID
HAVING COUNT(ORDER_ID)>=5
ORDER BY MONTH),
WEEKLY AS (
SELECT COUNT(SELLER_ID) WEEKLY_ACTIVE_SELLER, MONTH
FROM WEEKLY_TEMP
GROUP BY MONTH),
DAILY_TEMP AS (SELECT COUNT(ORDER_ID),SELLER_ID, DAY, MONTH
FROM CTE
GROUP BY DAY, MONTH, SELLER_ID
HAVING COUNT(ORDER_ID)>=1
ORDER BY MONTH),
DAILY AS (
SELECT COUNT(SELLER_ID) DAILY_ACTIVE_SELLER, MONTH
FROM DAILY_TEMP
GROUP BY MONTH)
SELECT MONTHLY.MONTH, MONTHLY.MONTHLY_ACTIVE_SELLER, WEEKLY.WEEKLY_ACTIVE_SELLER,DAILY_ACTIVE_SELLER
FROM MONTHLY
LEFT JOIN WEEKLY
ON MONTHLY.MONTH=WEEKLY.MONTH
LEFT JOIN DAILY
ON MONTHLY.MONTH=DAILY.MONTH