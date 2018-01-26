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
    
data_matrix[0][3] = '{"json_schema":"command"}'
data_matrix[1][3] = '{"json_schema":"response"}'
data_matrix[2][3] = '127.0.0.1'
data_matrix[3][3] = '1883'
data_matrix[4][3] = 'RootTopic'
          
        
for row in data_matrix:
    print row 
    
data_list = {}

for row in data_matrix:
    if not data_list.has_key(row[0]):
        data_list[row[0]] = {}
    else:
        data_list.get(row[0])[row[1]] = {}

# for row in data_matrix:
#     if data_list.get(row[0]) == row[0]:
                
        
            
        
    

print json.dumps(data_list) 
        
        