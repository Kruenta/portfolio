input = open('INPUT.txt', 'r')
content = input.read().split()
content = [int(i) for i in content]
content.sort()
first = content[0]
last = content[-1]
if  first >= 94 and last <= 727:
    out = str(last)
else:
    out = "Error"
output = open('OUTPUT.txt', 'w')
output.write(out)
output.close()
input.close()
