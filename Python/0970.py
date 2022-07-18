input = open('INPUT.txt', 'r')
content = input.read().split()
content = [int(i) for i in content]
if content[0] + content[1] == content[2] or content[1] + content[2] == content[0] or content[2] + content[0] == content[1]:
    out = 'YES'
else:
    out = 'NO'
output = open('OUTPUT.txt', 'w')
output.write(str(out))
output.close()
input.close()
