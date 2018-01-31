import json
from logzero import logger


# payload = '{"Type":"RESPONSE","Name":"applyConfiguration","Data":{"ResponseValue":{"ReconfiguredModules":["OpcUaConnector"],"ConfigurationType":"DELTA","ModuleConfigurationData":[{"ConfigurationData":{"OpcUa":{"Host":"10.0.0.24","Port":48010,"ServerName":"","Security":"NONE","MessageSecurityMode":"None","RequestedPublishingIntervalMs":10000,"MaxQueueSize":10,"MaxNotificationsPerPublish":1000},"Variables":[{"Identifier":"Demo.Dynamic.Scalar.Boolean","Namespace":"http://www.unifiedautomation.com/DemoServer/","IdType":"String","UpdateIntervalMs":10000}],"PayloadFormat":"{\n  \"Id\": \"<variableId>\",\n  \"Value\": \"<value>\",\n  \"Timestamp\": \"<timestamp>\",\n  \"TimestampSend\": \"<timestampSend>\"\n}"},"ConfigurationVersion":"0.1","ModuleName":"OpcUaConnector"}]},"ResultType":"SUCCESS"},"Tag":"11111111-1111-1111-1111-111111111111","TimeStamp":1517418942169}'

payload = '{"Data":{"ResponseValue":{"ModuleConfiguration":{"ConfigurationData":{"OpcUa":{"Host":"10.0.0.24","Port":48010,"ServerName":"","Security":"NONE","MessageSecurityMode":"None","RequestedPublishingIntervalMs":10000,"MaxQueueSize":10,"MaxNotificationsPerPublish":1000}}}}}}'



extractor = []

extractor.append('Data')

extractor.append('ResponseValue')
extractor.append('ModuleConfigurationData')
extractor.append('ConfigurationData')
extractor.append('OpcUa')

json_pl = json.loads(payload)

def unpack_json_string(json_string,key):
    json_object = json.loads(json_string)
    return json.dumps(json_object[key])

print unpack_json_string(payload, extractor[0])




# json_schema = """"""


# def unpack_json(json_string, key):
#     json_dict = json.loads(json_string)
#     return json.dumps(json_dict[key])
# 
# for key in extractor:        
#     print unpack_json(payload, key)        
                        

        
        
        

    
    

    