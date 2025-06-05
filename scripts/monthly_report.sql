SELECT district, COUNT(*) AS total_crimes, MAX(date) AS latest_incident
FROM crimes
GROUP BY district
ORDER BY total_crimes DESC;
