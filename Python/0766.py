input = open('INPUT.txt', 'r')
content = input.read().split()
first = int(content[0])
second = int(content[1])
needed = int(content[2])
if first * second < needed:
    out = "NO"
else:
    out = "YES"
output = open('OUTPUT.txt', 'w')
output.write(out)
output.close()
input.close()
