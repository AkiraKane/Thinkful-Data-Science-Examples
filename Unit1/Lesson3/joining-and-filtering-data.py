# Write a SQL statement which finds the mean of the average
# high temperatures for all of the cities within a state.

import sqlite3 as lite

con = lite.connect('my_database.db')

with con:
    cur = con.cursor()
    cur.execute("SELECT state AS 'State', AVG(avg_high) AS 'Avg High' FROM cities INNER JOIN weather ON (name = city) GROUP BY state HAVING AVG(avg_high) > 65 ORDER BY AVG(avg_high) DESC")
    rows = cur.fetchall()

print [desc[0] for desc in cur.description]
for row in rows:
    print row

# Here is the SQL statement from the above python code as it would appear in sqlite3:
'''
SELECT state AS 'State', AVG(avg_high) AS 'Avg High'
FROM cities
INNER JOIN weather ON (name = city)
GROUP BY (state)
HAVING AVG(avg_high) > 65
ORDER BY AVG(avg_high) DESC;
'''
