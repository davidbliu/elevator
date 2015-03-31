import psycopg2

try:
    conn = psycopg2.connect("dbname='elevator' user='postgres' host='localhost' password='password'")
except:
    print "I am unable to connect to the database"
