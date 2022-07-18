input_file = open('INPUT.txt', 'r')
content = input_file.read().split()
a = int(content[0])
b = int(content[1])
while a * b > 0:
    if a >= b:
        a = a % b
    else:
        b = b % a
output = open('OUTPUT.txt', 'w')
output.write(str(a + b))
output.close()
input_file.close()
