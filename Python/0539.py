input = open('INPUT.txt', 'r')
content = input.read()
first = int(content)
if first == 1:
    out = int(0)
elif first % 2 == 0:
    out = int(first / 2)
else:
    out = int(first)
output = open('OUTPUT.txt', 'w')
output.write(str(out))
output.close()
input.close()
