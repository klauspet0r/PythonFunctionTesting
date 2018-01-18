import json

json_string = '{"Test":{"Name":"getAvailableLogLevels","Description":"This test checks if the command getAvailableLogLevels works properly"},"TestDefinition":{"TestName":"getAvailableLogLevels","RobotCodeLocation":"./robot/getAvailableLogLevels.robot","Comment":"This is an comment about some robot stuff"},"Dependencies":{"Parameters":[{"domain":"messaging","name":"json_schema_command","version":0},{"domain":"messaging","name":"json_schema_response","version":1}]}}'

json_object = json.loads(json_string)


for entry in json_object.get("Dependencies").get("Parameters"):
    print 'domain is: {}, name is: {}, version is: {}'.format(entry.get("domain"), entry.get("name"), entry.get("version"))
    
    