import json

json_string = '{"Type":"RESPONSE","Name":"getSupportStatus","Data":{"ResponseValue":{"Message":"No Support Console is Running","TargetHost":"","TargetPort":0},"ResultType":"SUCCESS"},"Tag":"46528925-6021-3438-9773-997055251222","TimeStamp":1517239324927}'

json_object = json.loads(json_string)

content_to_check_for = 'No Support Console is Running'
    
for entry in json_object['Data']:
    if isinstance(json_object['Data'].get(entry), dict):
        sub_dict =  json_object['Data'].get(entry)
        print content_to_check_for in sub_dict.values()                                                        
    else:        
        print content_to_check_for in json_object['Data'].values()
