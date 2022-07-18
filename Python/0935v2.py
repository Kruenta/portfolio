input_file = open('INPUT.txt', 'r')  # 0943 0062
content = input_file.read().split()
kletkaA = int(content[0]) + int(content[1])
kletkaB = int(content[2]) + int(content[3])
if kletkaA % 2 == kletkaB % 2:
    out = "YES"
else:
    out = "NO"
output = open('OUTPUT.txt', 'w')
output.write(str(out))
output.close()
input_file.close()
