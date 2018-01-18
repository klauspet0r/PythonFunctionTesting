import sqlite3
import json

json_string = '{"Test":{"Name":"getAvailableLogLevels","Description":"This test checks if the command getAvailableLogLevels works properly"},"TestDefinition":{"TestName":"getAvailableLogLevels","RobotCodeLocation":"./robot/getAvailableLogLevels.robot","Comment":"This is an comment about some robot stuff"},"Dependencies":{"Parameters":[{"domain":"messaging","name":"json_schema_command","version":0},{"domain":"messaging","name":"json_schema_response","version":1}]}}'

json_object = json.loads(json_string)

db_adress = './TestSuiteDatabase.db'
conn = sqlite3.connect(db_adress)
c = conn.cursor()

c.execute('''SELECT EXISTS(SELECT * FROM Parameter WHERE Domain = 'messaging' AND Name = 'json_schema_command' AND Version = 0)''')

q_result =  c.fetchall()
print q_result[0][0]
