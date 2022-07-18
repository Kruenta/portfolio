input = open('INPUT.txt', 'r')
content = input.read().split()
content = [int(i) for i in content]
if content[0] * 2 < content[1] * 2 + content[2] * 2:
    out = 'NO'
else:
    out = 'YES'
output = open('OUTPUT.txt', 'w')
output.write(str(out))
output.close()
input.close()
