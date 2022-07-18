input_file = open('INPUT.txt', 'r')
content = input_file.read()
y = int(content)
k = 0
for i in range(1, int(content)):
    if y % i == 0:
        k += i
k = k + int(content)
output = open('OUTPUT.txt', 'w')
output.write(str(k))
output.close()
input_file.close()
