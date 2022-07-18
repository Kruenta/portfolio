input = open('INPUT.txt', 'r')
content = input.read()
first = int(content)
last = 9 - first
output = open('OUTPUT.txt', 'w')
output.write(str(first) + '9' + str(last))
output.close()
input.close()