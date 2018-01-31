import json
from logzero import logger
import pdb


# payload = '{"Type":"RESPONSE","Name":"applyConfiguration","Data":{"ResponseValue":{"ReconfiguredModules":["OpcUaConnector"],"ConfigurationType":"DELTA","ModuleConfigurationData":[{"ConfigurationData":{"OpcUa":{"Host":"10.0.0.24","Port":48010,"ServerName":"","Security":"NONE","MessageSecurityMode":"None","RequestedPublishingIntervalMs":10000,"MaxQueueSize":10,"MaxNotificationsPerPublish":1000},"Variables":[{"Identifier":"Demo.Dynamic.Scalar.Boolean","Namespace":"http://www.unifiedautomation.com/DemoServer/","IdType":"String","UpdateIntervalMs":10000}],"PayloadFormat":"{\n  \"Id\": \"<variableId>\",\n  \"Value\": \"<value>\",\n  \"Timestamp\": \"<timestamp>\",\n  \"TimestampSend\": \"<timestampSend>\"\n}"},"ConfigurationVersion":"0.1","ModuleName":"OpcUaConnector"}]},"ResultType":"SUCCESS"},"Tag":"11111111-1111-1111-1111-111111111111","TimeStamp":1517418942169}'

payload = '{"Data":{"ResponseValue":{"ModuleConfiguration":{"ConfigurationData":{"OpcUa":{"Host":"10.0.0.24","Port":48010,"ServerName":"","Security":"NONE","MessageSecurityMode":"None","RequestedPublishingIntervalMs":10000,"MaxQueueSize":10,"MaxNotificationsPerPublish":1000}}}}}}'



extractor = []
extractor.append('Data')
extractor.append('ResponseValue')
extractor.append('ModuleConfiguration')
extractor.append('ConfigurationData')
extractor.append('OpcUa')




def extract_sub_dict(js, extractor):
    jo = json.loads(js)
    sjonm1 = None        
    for k in extractor:
        if sjonm1 == None:
            sjo = jo[k] 
#             pdb.set_trace()                                   
        else:
            sjo = sjonm1[k]
#             pdb.set_trace()
            
        sjonm1 = sjo
                        
    return json.dumps(sjo)
        
print extract_sub_dict(payload,extractor)
        
        
   
            
    
            





# json_schema = """"""


# def unpack_json(json_string, key):
#     json_dict = json.loads(json_string)
#     return json.dumps(json_dict[key])
# 
# for key in extractor:        
#     print unpack_json(payload, key)        
                        

        
        
        

    
    

    