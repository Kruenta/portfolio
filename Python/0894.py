import math

input_file = open('INPUT.txt', 'r')
content = input_file.read().split()
sr = (math.pi * float(content[1]) * float(content[1])) - float(content[0])
r = math.sqrt(sr / math.pi)
output = open('OUTPUT.txt', 'w')
output.write(str('%.3f' % r))
output.close()
input_file.close()
