
import sys

import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

if len(sys.argv) != 2:
    print "Include 2 integers in the form k1,k2"
    exit(1)

input = sys.argv[1]

input = input.split(',')
if len(input) != 2:
    print "Incorrect k1,k2 argument"
    exit(1)
if len(input[0]) == 0 or len(input[1]) == 0:
    print "Incorrect k1,k2 argument"
    exit(1)
    
try:
    k1 = int(input[0])
    k2 = int(input[1])
except Exception as e:
    print "Could not convert to integer"
    exit(1)

if k1 > k2:
    print "k1 must be less than k2"
    exit(1)

conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")

cur = conn.cursor()
cur.execute("SELECT word, count FROM tweetwordcount ORDER BY count")
records = cur.fetchall()
for rec in records:
    if rec[1] >= k1 and rec[1] <= k2:
        print "%s: %d" %(rec[0], rec[1])

conn.commit()
