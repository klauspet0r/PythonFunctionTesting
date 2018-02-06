import json
from logzero import logger
from jsonschema import validate

# payload = '{"Type":"RESPONSE","Name":"applyConfiguration","Data":{"ResponseValue":{"ReconfiguredModules":["OpcUaConnector"],"ConfigurationType":"DELTA","ModuleConfigurationData":[{"ConfigurationData":{"OpcUa":{"Host":"10.0.0.24","Port":48010,"ServerName":"","Security":"NONE","MessageSecurityMode":"None","RequestedPublishingIntervalMs":10000,"MaxQueueSize":10,"MaxNotificationsPerPublish":1000},"Variables":[{"Identifier":"Demo.Dynamic.Scalar.Boolean","Namespace":"http://www.unifiedautomation.com/DemoServer/","IdType":"String","UpdateIntervalMs":10000}],"PayloadFormat":"{\n  \"Id\": \"<variableId>\",\n  \"Value\": \"<value>\",\n  \"Timestamp\": \"<timestamp>\",\n  \"TimestampSend\": \"<timestampSend>\"\n}"},"ConfigurationVersion":"0.1","ModuleName":"OpcUaConnector"}]},"ResultType":"SUCCESS"},"Tag":"11111111-1111-1111-1111-111111111111","TimeStamp":1517418942169}'

payload = """{
  "Type": "RESPONSE",
  "Name": "applyConfiguration",
  "Data": {
    "ResponseValue": {
      "ReconfiguredModules": [
        "OpcUaConnector",
        "DeviceLogger",
        "Uplink"
      ],
      "ConfigurationType": "DELTA",
      "ModuleConfigurationData": [                
        {
          "ConfigurationData": {
            "Variables": [
              {
                "UpdateIntervalMs": 10000,
                "IdType": "String",
                "Identifier": "",
                "Namespace": ""
              }
            ],
            "PayloadFormat": "",
            "OpcUa": {
              "ServerName": "",
              "RequestedPublishingIntervalMs": 10000,
              "Host": "10.0.0.24",
              "MaxQueueSize": 10,
              "MessageSecurityMode": "None",
              "Security": "NONE",
              "Port": 48010,
              "MaxNotificationsPerPublish": 1000
            }
          },
          "ConfigurationVersion": "0.1",
          "ModuleName": "OpcUaConnector"
        },        
        {
          "ConfigurationData": {
            "MqttEndpoints": [
              {
                "QoS": 1,
                "AuthenticationType": "None",
                "KeepAliveInterval": 2000,
                "Authentication": {
                  "UserName": "",
                  "UseSsl": false,
                  "RootCert": "",
                  "DeviceKey": "",
                  "DeviceId": "",
                  "UserCert": "",
                  "UserKey": "",
                  "Password": "",
                  "ExpiryTimeSeconds": 300
                },
                "ClientId": "client",
                "TopicMappings": {
                  "DeviceInput": [
                    {
                      "BrokerTopic": "device/configuration/in",
                      "DeviceTopic": "device/configuration"
                    },
                    {
                      "BrokerTopic": "device/information/in",
                      "DeviceTopic": "device/information"
                    },
                    {
                      "BrokerTopic": "system/modules/in",
                      "DeviceTopic": "system/modules"
                    },
                    {
                      "BrokerTopic": "system/network/in",
                      "DeviceTopic": "system/network"
                    },
                    {
                      "BrokerTopic": "system/control/in",
                      "DeviceTopic": "system/control"
                    },
                    {
                      "BrokerTopic": "device/log/in",
                      "DeviceTopic": "device/log"
                    },
                    {
                      "BrokerTopic": "system/monitor/in",
                      "DeviceTopic": "system/monitor"
                    },
                    {
                      "BrokerTopic": "dataconnector/opcua/in",
                      "DeviceTopic": "dataconnector/opcua"
                    },
                    {
                      "BrokerTopic": "system/support/in",
                      "DeviceTopic": "system/support"
                    }
                  ],
                  "DeviceOutput": [
                    {
                      "BrokerTopic": "device/configuration/out",
                      "DeviceTopic": "device/configuration"
                    },
                    {
                      "BrokerTopic": "device/information/out",
                      "DeviceTopic": "device/information"
                    },
                    {
                      "BrokerTopic": "system/modules/out",
                      "DeviceTopic": "system/modules"
                    },
                    {
                      "BrokerTopic": "system/network/out",
                      "DeviceTopic": "system/network"
                    },
                    {
                      "BrokerTopic": "device/log/out",
                      "DeviceTopic": "device/log"
                    },
                    {
                      "BrokerTopic": "system/control/out",
                      "DeviceTopic": "system/control"
                    },
                    {
                      "BrokerTopic": "system/monitor/out",
                      "DeviceTopic": "system/monitor"
                    },
                    {
                      "BrokerTopic": "dataconnector/opcua/out",
                      "DeviceTopic": "dataconnector/opcua"
                    },
                    {
                      "BrokerTopic": "system/support/out",
                      "DeviceTopic": "system/support"
                    },
                    {
                      "BrokerTopic": "log",
                      "DeviceTopic": "log"
                    },
                    {
                      "BrokerTopic": "data",
                      "DeviceTopic": "data/#"
                    },
                    {
                      "BrokerTopic": "data",
                      "DeviceTopic": "data"
                    },
                    {
                      "BrokerTopic": "heartbeat",
                      "DeviceTopic": "heartbeat"
                    }
                  ]
                },
                "MinimalSendIntervalMs": 1,
                "Host": "192.0.0.1",
                "RootTopic": "client",
                "MqttDestinationName": "DefaultLocalHost",
                "Port": 1883
              }
            ],
            "HeartbeatFormat": "<PlainTimestamp>"
          },
          "ConfigurationVersion": "0.1",
          "ModuleName": "Uplink"
        },
        {
          "ConfigurationData": {
            "LogForwarding": {
              "LeastSpecificLogLevel": "INFO"
            }
          },
          "ConfigurationVersion": "0.1",
          "ModuleName": "DeviceLogger"
        }
      ]
    },
    "ResultType": "SUCCESS"
  },
  "Tag": "65040870-5470-6126-0389-562163767229",
  "TimeStamp": 1517922163709
}"""



extractor = []
extractor.append('Data')
extractor.append('ResponseValue')
extractor.append('ModuleConfigurationData')


extractor_condition = []
extractor_condition.append('ConfigurationData')
extractor_condition.append('OpcUa')

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
                    
# def extract_sub_dict(js, extractor):
#     jo = json.loads(js)
#     sjonm1 = None        
#     for k in extractor:
#         print k
#         if sjonm1 == None:
#             if type(jo) == list:
#                 for element in jo:
#                     if k in element.keys():  
#                         sjo = element[k]
#                     else:
#                         return None
#             else:                
#                 if k in jo.keys():
#                     sjo = jo[k]                                                                    
#         else:
#             if type(sjonm1) == list:
#                 for element in sjonm1:
#                     if k in element.keys():  
#                         sjo = element[k]
#             else:
#                 sjo = sjonm1[k]  
#         sjonm1 = sjo
#                          
#     return json.dumps(sjo)
# 
# print extract_sub_dict(payload,extractor)

def unpack_json_string(js, extractor, extractor_condition=None):        
    def unpack_json_object(_jo,_extractor):        
        if len(_extractor) == 1:
            return _jo[_extractor[0]] if _extractor[0] in _jo.keys() else None        
        elif len(_extractor) == 0:            
            print 'verkackt'
            return None
        else:
            if type(_jo) == dict:
                return unpack_json_object(_jo[_extractor[0]] if _extractor[0] in _jo.keys() else None, _extractor[1:])
            elif type(_jo) == list:
                for sjo in _jo:
                    sjro = unpack_json_object(sjo[_extractor[0]] if _extractor[0] in sjo.keys() else None, _extractor[1:])  # jsro = sub json return object
                    if sjro is not None:
                        return sjro
                return None
                         
            else:
                print 'verkackt'
                return None
    jo = json.loads(js)
    ejo = unpack_json_object(jo, extractor)
    if extractor_condition is None:
        return json.dumps(ejo)
    else:
        if type(ejo) == dict:
            if unpack_json_object(ejo, extractor_condition) is not None:
                return json.dumps(ejo)
            else:
                return None            
        elif type(ejo) == list: 
            for entry in ejo:
                if unpack_json_object(entry, extractor_condition) is not None:
                    return json.dumps(entry)
            return None
        else:
            return None      


print unpack_json_string(payload, extractor, extractor_condition)


# print validate(json.loads(extract_sub_dict(payload, extractor)), json.loads(json_schema))
# print validate(json.loads(unpack_json_string(payload, extractor)), json.loads(json_schema)) 





