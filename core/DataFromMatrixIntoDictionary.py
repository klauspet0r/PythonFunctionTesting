from random import randint
import json
from docutils.nodes import row

data_matrix = [[0 for x in range(4)] for x in range(5)]

for i in range(len(data_matrix)):
    data_matrix[i][0] = 'messaging'    
        
for row in data_matrix:
    for i in range(len(row)):
        if i != 0:
            row[i] = i

data_matrix[0][1] = 'command'
data_matrix[1][1] = 'response'
data_matrix[2][1] = 'host'
data_matrix[3][1] = 'port'
data_matrix[4][1] = 'roottopic'  

for i in range(0,4):
    data_matrix[i][2] = i
    
data_matrix[0][3] = 'json_schema_command'
data_matrix[1][3] = 'json_schema_response'
data_matrix[2][3] = '127.0.0.1'
data_matrix[3][3] = '1883'
data_matrix[4][3] = 'RootTopic'
          
        
for row in data_matrix:
    print row 
    
data_dict = {}

for row in data_matrix:
    sub_dict = data_dict
    for key in row[:-2]:
        if not sub_dict.has_key(key):
            sub_dict[key] = {}
        sub_dict = sub_dict[key]
    sub_dict[row[-2]] = row[-1]


print ''        
print json.dumps(data_dict)



with open('test_suite_parameter.json', "w") as text_file:
    text_file.write(json.dumps(data_dict))
                
json_file = open('test_suite_parameter.json',"r")

json_object = json.loads(json_file.read())

for key,value in json_object['messaging'].get('command').iteritems():
    print key,value



