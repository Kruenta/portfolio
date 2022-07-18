import math

input_file = open('INPUT.txt', 'r')
content = input_file.read().split()
a = math.sqrt(int(content[0]) * int(content[1]))
b = math.sqrt(float(content[0]) * float(content[1]))
a = int(a)
print(a, b)
if a == b:
    out = math.sqrt(int(content[0]) * int(content[1]))
else:
    out = 0
out = int(out)
output = open('OUTPUT.txt', 'w')
output.write(str(out))
output.close()
input_file.close()
