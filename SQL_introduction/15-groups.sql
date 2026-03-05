-- Lists the number of records with the same score in the table second_table
-- The result should display: the score and the number of records (labeled 'number')
-- The list should be sorted by the number of records (descending)
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;