import json


payload = '{"Type":"RESPONSE","Name":"getSupportStatus","Data":{"ResponseValue":{"Message":"No Support Console is Running","TargetHost":"","TargetPort":0},"ResultType":"SUCCESS"},"Tag":"46528925-6021-3438-9773-997055251222","TimeStamp":1517239324927}'

payload_match = '{"Data":{"ResponseValue":{"Message":"No Support Console is Running"}}}'


payload_match1 = ["Data","ResponseValue","Message","No Support Console is Running"]
payload_match2 = ["Data","ResponseValue","Message"]

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

# def check_content(small, big):
#         small_json = json.loads(small)
#         big_json = json.loads(big)        
#     
#         def match_dicts(small,big):    
#             if type(big) != type(small):
#                 return False
#             if type(small) != dict:
#                 return (small == big)
#             for key in big.keys():        
#                 if key == small.keys()[0]:     
#                     if match_dicts(small[key],big[key]) or match_dicts(small,big[key]):
#                         return True
#                     else:
#                         continue
#             return False
#         
#         return match_dicts(small_json, big_json)
            
            
print check_content(payload, payload_match1)
print check_content(payload, payload_match2)
