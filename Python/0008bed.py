input = open('INPUT.txt', 'r')
content = input.read().split()
first = int(content[0])
second = int(content[1])
if first < second:
    out = "<"
elif  first > second:
    out = ">"
else:
    out = "="
output = open('OUTPUT.txt', 'w')
output.write(out)
output.close()
input.close()
