input = open('INPUT.txt', 'r')
content = input.read()
if content[0] == content[3] and content[1] == content[2]:
    out = "YES"
else:
    out = "NO"
output = open('OUTPUT.txt', 'w')
output.write(str(out))
output.close()
input.close()