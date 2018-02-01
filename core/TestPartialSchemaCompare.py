import json
from logzero import logger

# payload = '{"Type":"RESPONSE","Name":"applyConfiguration","Data":{"ResponseValue":{"ReconfiguredModules":["OpcUaConnector"],"ConfigurationType":"DELTA","ModuleConfigurationData":[{"ConfigurationData":{"OpcUa":{"Host":"10.0.0.24","Port":48010,"ServerName":"","Security":"NONE","MessageSecurityMode":"None","RequestedPublishingIntervalMs":10000,"MaxQueueSize":10,"MaxNotificationsPerPublish":1000},"Variables":[{"Identifier":"Demo.Dynamic.Scalar.Boolean","Namespace":"http://www.unifiedautomation.com/DemoServer/","IdType":"String","UpdateIntervalMs":10000}],"PayloadFormat":"{\n  \"Id\": \"<variableId>\",\n  \"Value\": \"<value>\",\n  \"Timestamp\": \"<timestamp>\",\n  \"TimestampSend\": \"<timestampSend>\"\n}"},"ConfigurationVersion":"0.1","ModuleName":"OpcUaConnector"}]},"ResultType":"SUCCESS"},"Tag":"11111111-1111-1111-1111-111111111111","TimeStamp":1517418942169}'

payload = """{"Data":{"ResponseValue":{"ModuleConfiguration":{"ConfigurationData":
                {"OpcUa":{"Host":"10.0.0.24","Port":48010,"ServerName":"",
                "Security":"NONE","MessageSecurityMode":"None",
                "RequestedPublishingIntervalMs":10000,"MaxQueueSize":10,
                "MaxNotificationsPerPublish":1000}}}}}}"""



extractor = []
extractor.append('Data')
extractor.append('ResponseValue')
extractor.append('ModuleConfiguration')
extractor.append('ConfigurationData')
extractor.append('OpcUa')

json_schema = """{"$schema":"http://json-schema.org/draft-04/schema#","title":
                    "Opc Ua Config","type":"object","additionalProperties":false,
                    "properties":{"ServerName":{"type":"string"},
                    "RequestedPublishingIntervalMs":{"type":"integer"},
                    "Host":{"type":"string"},"MaxQueueSize":{"type":"integer"},
                    "MessageSecurityMode":{"type":"string"},
                    "Security":{"type":"string"},"Port":{"type":"integer"},
                    "MaxNotificationsPerPublish":{"type":"integer"}},
                    "required":["ServerName","RequestedPublishingIntervalMs",
                    "Host","MaxQueueSize","MessageSecurityMode","Security",
                    "Port","MaxNotificationsPerPublish"]}"""




def extract_sub_dict(js, extractor):
    jo = json.loads(js)
    sjonm1 = None        
    for k in extractor:
        if sjonm1 == None:
            sjo = jo[k]                                    
        else:
            sjo = sjonm1[k]            
        sjonm1 = sjo
                         
    return json.dumps(sjo)

print extract_sub_dict(payload,extractor)

def unpack_json_string(js,extractor):        
    def unpack_json_object(_jo,_extractor):        
        if len(_extractor) == 1:
            return _jo[_extractor[0]]
        elif len(_extractor) == 0:
            print 'verkackt'
            return None
        else:
            return unpack_json_object(_jo[_extractor[0]], _extractor[1:])

    jo = json.loads(js)
    return json.dumps(unpack_json_object(jo, extractor))


print unpack_json_string(payload, extractor)


            



    