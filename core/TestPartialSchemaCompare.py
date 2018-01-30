import json


payload = '{"Type":"RESPONSE","Name":"getSupportStatus","Data":{"ResponseValue":{"Message":"No Support Console is Running","TargetHost":"","TargetPort":0},"ResultType":"SUCCESS"},"Tag":"46528925-6021-3438-9773-997055251222","TimeStamp":1517239324927}'

payload_match = '{"Data":{"ResponseValue":{"Message":"No Support Console is Running"}}}'


def check_content(small, big):
        small_json = json.loads(small)
        big_json = json.loads(big)        
    
        def match_dicts(small,big):    
            if type(big) != type(small):
                return False
            if type(small) != dict:
                return (small == big)
            for key in big.keys():        
                if key == small.keys()[0]:     
                    if match_dicts(small[key],big[key]) or match_dicts(small,big[key]):
                        return True
                    else:
                        continue
            return False
        
        return match_dicts(small_json, big_json)
            
            
print check_content(payload_match, payload)                 