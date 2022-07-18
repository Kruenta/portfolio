input = open('INPUT.txt', 'r')
content = input.read().split()
content = [int(i) for i in content]
if content[0] >= content[2] * 2 and content[1] >= content[2] * 2:
    out = 'YES'
else:
    out = 'NO'
output = open('OUTPUT.txt', 'w')
output.write(str(out))
output.close()
input.close()
