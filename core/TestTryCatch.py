import sqlite3 
import json
from logzero import logger
import sys




json_string = '{"Test":{"Name":"getAvailableLogLevels","Description":"This test checks if the command getAvailableLogLevels works properly"},"TestDefinition":{"TestName":"getAvailableLogLevels","RobotCodeLocation":"./robot/getAvailableLogLevels.robot","Comment":"This is an comment about some robot stuff"},"Dependencies":{"Parameters":[{"domain":"messaging","name":"json_schema_command","version":0},{"domain":"mmessaging","name":"json_schema_response","version":1}]}}'

json_object = json.loads(json_string)

db_adress = './TestSuiteDatabase.db'
conn = sqlite3.connect(db_adress)

# sqlite3.Time



c = conn.cursor()

try:
    for entry in json_object.get("Dependencies").get("Parameters"):
        c.execute('''SELECT EXISTS(SELECT * FROM Parameter WHERE Domain = '{}' AND Name = '{}' AND Version = '{}')'''.format(entry.get("domain"), entry.get("name"), entry.get("version")))
        q_result = c.fetchall()
        if q_result[0][0] == 0:
            raise sqlite3.IntegrityError
except sqlite3.IntegrityError:
    logger.error("You are trying to add a test with a dependency that does not exist in the database")
    sys.exit('')
    
logger.info("All good!")
    
                