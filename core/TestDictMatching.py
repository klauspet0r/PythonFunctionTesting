import json

payload = json.loads('{"Type":"RESPONSE","Name":"getSupportStatus","Data":{"ResponseValue":{"Message":"No Support Console is Running","TargetHost":"","TargetPort":0},"ResultType":"SUCCESS"},"Tag":"46528925-6021-3438-9773-997055251222","TimeStamp":1517239324927}')

payload_match = json.loads('{"Data":{"ResponseValue":{"Message":"No Support Console is Running"}}}')


def match_dicts(small, big):    
    if type(big) != type(small):
        return False
    if type(small) != dict:
        return (small == big)
    for key in big.keys():        
        if key == small.keys()[0]:
            if match_dicts(small[key],big[key]):
                return True
            else:
                continue
    return False
            
            
print match_dicts(payload_match, payload)                 