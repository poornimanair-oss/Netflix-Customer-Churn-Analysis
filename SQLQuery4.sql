SELECT COUNT(*) AS Total_Customers
FROM netflix_customers;
SELECT
    Churn_Status,
    COUNT(*) AS Customer_Count
FROM netflix_customers
GROUP BY Churn_Status;
SELECT
    Subscription_Plan,
    COUNT(*) AS Churned_Customers
FROM netflix_customers
WHERE Churn_Status = 'Yes'
GROUP BY Subscription_Plan
ORDER BY Churned_Customers DESC;
SELECT
    Region,
    COUNT(*) AS Churned_Customers
FROM netflix_customers
WHERE Churn_Status = 'Yes'
GROUP BY Region
ORDER BY Churned_Customers DESC;
SELECT
    Churn_Status,
    AVG(Customer_Satisfaction_Score) AS Avg_Satisfaction
FROM netflix_customers
GROUP BY Churn_Status;
SELECT
    Churn_Status,
    AVG(Daily_Watch_Time_Hours) AS Avg_Watch_Time
FROM netflix_customers
GROUP BY Churn_Status;
SELECT
    Payment_History,
    COUNT(*) AS Customers,
    SUM(CASE WHEN Churn_Status = 'Yes' THEN 1 ELSE 0 END) AS Churned_Customers,
    ROUND(
        100.0 * SUM(CASE WHEN Churn_Status = 'Yes' THEN 1 ELSE 0 END) / COUNT(*),
        2
    ) AS Churn_Rate
FROM netflix_customers
GROUP BY Payment_History;
SELECT
    Churn_Status,
    AVG(Engagement_Rate) AS Avg_Engagement
FROM netflix_customers
GROUP BY Churn_Status;
SELECT
    Churn_Status,
    AVG(Support_Queries_Logged) AS Avg_Support_Queries
FROM netflix_customers
GROUP BY Churn_Status;
SELECT
    Churn_Status,
    AVG(Subscription_Length_Months) AS Avg_Subscription_Length
FROM netflix_customers
GROUP BY Churn_Status;
SELECT
    Churn_Status,
    AVG(Age) AS Avg_Age
FROM netflix_customers
GROUP BY Churn_Status;
SELECT
    Subscription_Plan,
    COUNT(*) AS Total_Customers,
    SUM(CASE WHEN Churn_Status='Yes' THEN 1 ELSE 0 END) AS Churned_Customers,
    ROUND(
        100.0 * SUM(CASE WHEN Churn_Status='Yes' THEN 1 ELSE 0 END) / COUNT(*),
        2
    ) AS Churn_Rate
FROM netflix_customers
GROUP BY Subscription_Plan
ORDER BY Churn_Rate DESC;
SELECT
    Device_Used_Most_Often,
    COUNT(*) AS Total_Customers,
    SUM(CASE WHEN Churn_Status='Yes' THEN 1 ELSE 0 END) AS Churned_Customers,
    ROUND(
        100.0 * SUM(CASE WHEN Churn_Status='Yes' THEN 1 ELSE 0 END) / COUNT(*),
        2
    ) AS Churn_Rate
FROM netflix_customers
GROUP BY Device_Used_Most_Often
ORDER BY Churn_Rate DESC;