\prompt 'input reciept id to see customer data: '  userINP

SELECT 
    c.CUSTOMER_ID,
    c.FIRST_NAME,
    c.LAST_NAME,
    c.PHONE_NUMBER,
    c.REWARDS_POINTS
FROM CUSTOMER c
JOIN RECEIPT r ON c.CUSTOMER_ID = r.CUSTOMER_ID
WHERE r.RECEIPT_ID = :userINP;  -- Replace with your receipt ID
