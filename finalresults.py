
import sys

import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")


if len(sys.argv) != 2:
    cur = conn.cursor()
    cur.execute("SELECT word, count FROM tweetwordcount ORDER BY word")
    records = cur.fetchall()
    for rec in records:
        print rec    
    conn.commit()
    exit(0)

word = str(sys.argv[1]).lower()
    
cur = conn.cursor()

cur.execute("SELECT word, count FROM tweetwordcount WHERE word = %s", (word,))
records = cur.fetchall()
if len(records) == 0:
    print "Word not present in stream"
else:
    for rec in records:
        print "Total number of occurrences of \"%s\": %d" %(rec[0], rec[1])

conn.commit()



