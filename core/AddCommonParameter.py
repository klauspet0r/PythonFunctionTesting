import sqlite3
import argparse


parser = argparse.ArgumentParser(description='Insert Values into the Parameter table')

parser.add_argument('--dom', action='store', dest='domain', help='Store parameter domain')
parser.add_argument('--nam', action='store', dest='name', help='Store parameter name')
parser.add_argument('--dat', action='store', dest='data', help='Store parameter data/value')

results = parser.parse_args()

db_adress = './TestSuiteDatabase.db'
conn = sqlite3.connect(db_adress)
c = conn.cursor()

c.execute("SELECT MAX(Version) FROM Parameter")

q_result = c.fetchall()

if q_result[0][0] is None:
    q_result = 0
    
else:
    q_result = int(q_result[0][0])+1

c.execute("INSERT INTO Parameter (Domain, Name, Version, Data) VALUES ('{}','{}','{}','{}')".format(results.domain, results.name, q_result, results.data))
conn.commit()
conn.close()
