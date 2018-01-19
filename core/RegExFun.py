import re


with open('getCpuUsage.robot') as robot_file:
    robot_string = robot_file.read()
    
regex_pattern_object = re.compile('\*{3} Variables \*{3}')

for x in regex_pattern_object.findall(robot_string):
    print x

print re.sub('\*{3} +Variables +\*{3}', '*** Variables ***\n${var1}  value1\n${var2}  value2 ', robot_string)