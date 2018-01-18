#!/bin/bash

rm TestSuiteDatabase.db
python CreateSqliteDbForM2cpTesting.py
python AddCommonParameter.py --dom messaging --nam json_schema_command --dat '{"$schema":"http://json-schema.org/draft-04/schema#","title":"Command","type":"object","additionalProperties":false,"properties":{"Type":{"type":"string"},"Name":{"type":"string"},"Tag":{"type":"string"},"TimeStamp":{"type":"integer"},"Data":{}},"required":["Type","Name","Tag","TimeStamp","Data"]}'
python AddCommonParameter.py --dom messaging --nam json_schema_response --dat '{"$schema":"http://json-schema.org/draft-04/schema#","title":"Response Message","type":"object","additionalProperties":false,"properties":{"Type":{"type":"string","enum":["COMMAND","RESPONSE","ERROR","SIGNAL"],"description":"The message type."},"Name":{"type":"string","description":"The message name."},"Data":{"description":"The message data. A JSON object."},"Tag":{"type":"string","description":"The message tag providing unique identification."},"TimeStamp":{"type":"integer","description":"The message timestamp."}},"required":["TimeStamp"]}'
python WriteTestIntoDatabase.py --json_location ./json/TestDefinition.json
