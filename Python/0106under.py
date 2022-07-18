input = open('INPUT.txt', 'r')
content = input.read().split()
num1 = content[1:].count('1')
num2 = content[1:].count('0')
if num1 < num2:
    out = num1
else:
    out = num2
output = open('OUTPUT.txt', 'w')
output.write(str(out))
output.close()
input.close()
