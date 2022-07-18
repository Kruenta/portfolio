input = open('INPUT.txt', 'r')
content = input.read().split()
num1 = 0
num2 = 0
for i in content[1:]:
    if i == '1':
        num1 = num1 + 1
    elif i == '0':
        num2 = num2 + 1
if num1 < num2:
    out = num1
else:
    out = num2
output = open('OUTPUT.txt', 'w')
output.write(str(out))
output.close()
input.close()
