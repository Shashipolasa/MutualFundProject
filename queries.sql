-- 1. Top 5 mutual funds by AUM
SELECT scheme_name, fund_house, aum_crore
FROM scheme_performance
ORDER BY aum_crore DESC
LIMIT 5;

-- 2. Average NAV for each fund
SELECT amfi_code, AVG(nav) AS avg_nav
FROM nav_history
GROUP BY amfi_code;

-- 3. Total SIP investment amount by state
SELECT state, SUM(amount_inr) AS total_sip_amount
FROM investor_transactions
WHERE transaction_type = 'Sip'
GROUP BY state
ORDER BY total_sip_amount DESC;

-- 4. Top 10 cities by transaction volume
SELECT city, COUNT(*) AS transaction_count
FROM investor_transactions
GROUP BY city
ORDER BY transaction_count DESC
LIMIT 10;

-- 5. Funds with expense ratio below 1%
SELECT scheme_name, expense_ratio_pct
FROM scheme_performance
WHERE expense_ratio_pct < 1;

-- 6. Average 1-year return by category
SELECT category, AVG(return_1yr_pct) AS avg_return
FROM scheme_performance
GROUP BY category;

-- 7. Number of investors by city tier
SELECT city_tier, COUNT(DISTINCT investor_id) AS investor_count
FROM investor_transactions
GROUP BY city_tier;

-- 8. Transaction amount by payment mode
SELECT payment_mode, SUM(amount_inr) AS total_amount
FROM investor_transactions
GROUP BY payment_mode
ORDER BY total_amount DESC;

-- 9. Distribution of funds by risk grade
SELECT risk_grade, COUNT(*) AS fund_count
FROM scheme_performance
GROUP BY risk_grade;

-- 10. Top performing funds based on 3-year returns
SELECT scheme_name, return_3yr_pct
FROM scheme_performance
ORDER BY return_3yr_pct DESC
LIMIT 10;