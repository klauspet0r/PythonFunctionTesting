import json

json_string = '{"Type":"RESPONSE","Name":"getSupportStatus","Data":{"ResponseValue":{"Message":"No Support Console is Running","TargetHost":"","TargetPort":0},"ResultType":"SUCCESS"},"Tag":"46528925-6021-3438-9773-997055251222","TimeStamp":1517239324927}'

json_object = json.loads(json_string)

content_to_check_for = 'No Support Console is Running'
    
print content_to_check_for in json_object['Data'].get('ResponseValue').values()