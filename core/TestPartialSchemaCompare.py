import json
from jsonschema import validate

payload = """{
  "Type": "RESPONSE",
  "Name": "applyConfiguration",
  "Data": {
    "ResponseValue": {
      "ReconfiguredModules": [
        "Uplink"
      ],
      "ConfigurationType": "DELTA",
      "ModuleConfigurationData": [
        {
          "ConfigurationData": {
            "MqttEndpoints": [
              {
                "MqttDestinationName": "DefaultLocalHost",
                "ClientId": "client",
                "MinimalSendIntervalMs": 1,
                "Port": 1883,
                "KeepAliveInterval": 2000,
                "QoS": 1,
                "Host": "192.0.0.1",
                "RootTopic": "client",
                "AuthenticationType": "None",
                "Authentication": {
                  "UserName": "",
                  "Password": "",
                  "DeviceKey": "",
                  "DeviceId": "",
                  "ExpiryTimeSeconds": 300,
                  "UseSsl": false,
                  "RootCert": "",
                  "UserCert": "",
                  "UserKey": ""
                },
                "TopicMappings": {
                  "DeviceInput": [
                    {
                      "DeviceTopic": "device/configuration",
                      "BrokerTopic": "device/configuration/in"
                    },
                    {
                      "DeviceTopic": "device/information",
                      "BrokerTopic": "device/information/in"
                    },
                    {
                      "DeviceTopic": "system/modules",
                      "BrokerTopic": "system/modules/in"
                    },
                    {
                      "DeviceTopic": "system/network",
                      "BrokerTopic": "system/network/in"
                    },
                    {
                      "DeviceTopic": "system/control",
                      "BrokerTopic": "system/control/in"
                    },
                    {
                      "DeviceTopic": "device/log",
                      "BrokerTopic": "device/log/in"
                    },
                    {
                      "DeviceTopic": "system/monitor",
                      "BrokerTopic": "system/monitor/in"
                    },
                    {
                      "DeviceTopic": "dataconnector/opcua",
                      "BrokerTopic": "dataconnector/opcua/in"
                    },
                    {
                      "DeviceTopic": "system/support",
                      "BrokerTopic": "system/support/in"
                    }
                  ],
                  "DeviceOutput": [
                    {
                      "DeviceTopic": "device/configuration",
                      "BrokerTopic": "device/configuration/out"
                    },
                    {
                      "DeviceTopic": "device/information",
                      "BrokerTopic": "device/information/out"
                    },
                    {
                      "DeviceTopic": "system/modules",
                      "BrokerTopic": "system/modules/out"
                    },
                    {
                      "DeviceTopic": "system/network",
                      "BrokerTopic": "system/network/out"
                    },
                    {
                      "DeviceTopic": "device/log",
                      "BrokerTopic": "device/log/out"
                    },
                    {
                      "DeviceTopic": "system/control",
                      "BrokerTopic": "system/control/out"
                    },
                    {
                      "DeviceTopic": "system/monitor",
                      "BrokerTopic": "system/monitor/out"
                    },
                    {
                      "DeviceTopic": "dataconnector/opcua",
                      "BrokerTopic": "dataconnector/opcua/out"
                    },
                    {
                      "DeviceTopic": "system/support",
                      "BrokerTopic": "system/support/out"
                    },
                    {
                      "DeviceTopic": "log",
                      "BrokerTopic": "log"
                    },
                    {
                      "DeviceTopic": "data/#",
                      "BrokerTopic": "data"
                    },
                    {
                      "DeviceTopic": "data",
                      "BrokerTopic": "data"
                    },
                    {
                      "DeviceTopic": "heartbeat",
                      "BrokerTopic": "heartbeat"
                    }
                  ]
                }
              },
              {
                "MqttDestinationName": "AzureIotHub",
                "ClientId": "igusSmartChain2",
                "MinimalSendIntervalMs": 1,
                "Port": 8883,
                "KeepAliveInterval": 2000,
                "QoS": 1,
                "Host": "MichalsSmartChainHub.azure-devices.net",
                "RootTopic": "devices/igusSmartChain2/messages/events/",
                "AuthenticationType": "AzureSasCredentials",
                "Authentication": {
                  "UserName": "MichalsSmartChainHub.azure-devices.net/igusSmartChain2",
                  "Password": "",
                  "DeviceKey": "aL/MV7GhPLIe1V/7ckVcJSrJXI8fyI2w4Az3Wvcp70k=",
                  "DeviceId": "igusSmartChain2",
                  "ExpiryTimeSeconds": 300,
                  "UseSsl": true,
                  "RootCert": "",
                  "UserCert": "",
                  "UserKey": ""
                },
                "TopicMappings": {
                  "DeviceInput": [
                    {
                      "DeviceTopic": "runtime/configuration",
                      "BrokerTopic": "runtime"
                    },
                    {
                      "DeviceTopic": "runtime/information/messaging",
                      "BrokerTopic": "runtime"
                    },
                    {
                      "DeviceTopic": "runtime/installation",
                      "BrokerTopic": "runtime"
                    },
                    {
                      "DeviceTopic": "network",
                      "BrokerTopic": "network"
                    },
                    {
                      "DeviceTopic": "system/control",
                      "BrokerTopic": "system"
                    }
                  ],
                  "DeviceOutput": [
                    {
                      "DeviceTopic": "runtime/configuration",
                      "BrokerTopic": "runtime"
                    },
                    {
                      "DeviceTopic": "runtime/information/messaging",
                      "BrokerTopic": "runtime"
                    },
                    {
                      "DeviceTopic": "runtime/installation",
                      "BrokerTopic": "runtime"
                    },
                    {
                      "DeviceTopic": "network",
                      "BrokerTopic": "network"
                    },
                    {
                      "DeviceTopic": "system/control",
                      "BrokerTopic": "system"
                    },
                    {
                      "DeviceTopic": "log",
                      "BrokerTopic": "log"
                    },
                    {
                      "DeviceTopic": "data",
                      "BrokerTopic": "data"
                    },
                    {
                      "DeviceTopic": "heartbeat",
                      "BrokerTopic": "heartbeat"
                    },
                    {
                      "DeviceTopic": "data/#",
                      "BrokerTopic": "data"
                    }
                  ]
                }
              }
            ],
            "HeartbeatFormat": "<PlainTimestamp>"
          },
          "ConfigurationVersion": "0.1",
          "ModuleName": "Uplink"
        }
      ]
    },
    "ResultType": "SUCCESS"
  },
  "Tag": "11111111-1111-1111-1111-111111111111",
  "TimeStamp": 1518001128607
}"""

extractor = []
extractor.append('Data')
extractor.append('ResponseValue')
extractor.append('ModuleConfigurationData')
extractor.append('ConfigurationData')


json_schema = """{
  "$schema": "http://json-schema.org/draft-04/schema#",
  "title": "Uplink Configuration",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "MqttEndpoints": {
      "type": "array",
      "items": {
        "$ref": "#/definitions/MqttConfiguration"
      }
    },
    "HeartbeatFormat": {
      "type": "string",
      "description": "Format string for heartbeat formatting. Replacables (brackets included): <PlainTimestamp> (long / milliseconds since the epoch); <FormattedTimestamp> (string formatted in UTC time)"
    }
  },
  "definitions": {
    "MqttConfiguration": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "MqttDestinationName": {
          "type": "string"
        },
        "ClientId": {
          "type": "string"
        },
        "MinimalSendIntervalMs": {
          "type": "integer",
          "minimum": 1
        },
        "Port": {
          "type": "integer",
          "minimum": 1
        },
        "KeepAliveInterval": {
          "type": "integer",
          "minimum": 1
        },
        "QoS": {
          "type": "integer"
        },
        "Host": {
          "type": "string"
        },
        "RootTopic": {
          "type": "string"
        },
        "AuthenticationType": {
          "type": "string"
        },
        "Authentication": {
          "$ref": "#/definitions/AuthenticationConfiguration"
        },
        "TopicMappings": {
          "$ref": "#/definitions/TopicMappings"
        }
      },
      "required": [
        "MqttDestinationName",
        "ClientId",
        "MinimalSendIntervalMs",
        "Port",
        "KeepAliveInterval",
        "QoS",
        "Host",
        "RootTopic",
        "AuthenticationType",
        "TopicMappings"
      ]
    },
    "AuthenticationConfiguration": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "UserName": {
          "type": "string"
        },
        "Password": {
          "type": "string"
        },
        "DeviceKey": {
          "type": "string"
        },
        "DeviceId": {
          "type": "string"
        },
        "ExpiryTimeSeconds": {
          "type": "integer"
        },
        "UseSsl": {
          "type": "boolean"
        },
        "RootCert": {
          "type": "string"
        },
        "UserCert": {
          "type": "string"
        },
        "UserKey": {
          "type": "string"
        }
      }
    },
    "TopicMappings": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "DeviceInput": {
          "type": "array",
          "items": {
            "$ref": "#/definitions/MappingEntry"
          }
        },
        "DeviceOutput": {
          "type": "array",
          "items": {
            "$ref": "#/definitions/MappingEntry"
          }
        }
      },
      "required": [
        "DeviceInput",
        "DeviceOutput"
      ]
    },
    "MappingEntry": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "DeviceTopic": {
          "type": "string"
        },
        "BrokerTopic": {
          "type": "string"
        }
      },
      "required": [
        "DeviceTopic",
        "BrokerTopic"
      ]
    }
  }
}"""
                
def match_content(_payload, _condition):
    if len(_condition) == 0:
        return True
    else:
        if type(_payload)== dict:
            if _condition[0] in _payload.keys():
                return match_content(_payload[_condition[0]], _condition[1:])
            else:
                return False
        elif type(_payload)== list:
            return any([match_content(element, _condition) for element in _payload])                                    
        else:
            if len(_condition) == 1 and _condition[0] == _payload:
                return True
            else:
                return False

def check_content(payload, condition):
    payload_json = json.loads(payload)        
    return match_content(payload_json, condition)   

def unpack_json_string(js, extractor, extractor_condition=None):        
    def unpack_json_object(_jo,_extractor):        
        #if len(_extractor) == 1:
            #if type(_jo) == dict:
            #return _jo[_extractor[0]] if _extractor[0] in _jo.keys() else None
            #if type(_jo) == list:                                    
        if len(_extractor) == 0:                        
            return _jo
        else:
            if type(_jo) == dict:
                return unpack_json_object(_jo[_extractor[0]] , _extractor[1:]) if _extractor[0] in _jo.keys() else None
            elif type(_jo) == list:
                for sjo in _jo:
                    sjro = unpack_json_object(sjo[_extractor[0]] , _extractor[1:]) if _extractor[0] in sjo.keys() else None # jsro = sub json return object
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
            if match_content(ejo, extractor_condition):
                return json.dumps(ejo)
            else:
                return None            
        elif type(ejo) == list:
            ejod = [element for element in ejo if match_content(element, extractor_condition)]
            if len(ejod) > 0:
                return json.dumps(ejod)
            else:
                return None                
        else:
            return None      


print unpack_json_string(payload, extractor)

print validate(json.loads(unpack_json_string(payload, extractor)), json.loads(json_schema)) 





