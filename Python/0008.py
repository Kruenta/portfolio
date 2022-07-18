input = open('INPUT.txt', 'r')
content = input.read().split()
first = int(content[0])
second = int(content[1])
last = int(content[2])
if first * second == last:
    out = "YES"
else:
    out = "NO"
output = open('OUTPUT.txt', 'w')
output.write(out)
output.close()
input.close()
