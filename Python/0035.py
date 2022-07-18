input_file = open('INPUT.txt', 'r')
content = input_file.read().split()
key = [int(x) for x in content[1:]]
m = []
n = []
for i in range(0, len(key)):
    if i % 2 == 0:
        n.append(key[i])
    if i % 2 != 0:
        m.append(key[i])
out = [int(19 * mi + (ni + 239) * (ni + 366) / 2) for mi, ni in zip(m, n)]
out = [str(v) for v in out]
out = "\n".join(out)
output = open('OUTPUT.txt', 'w')
output.write(str(out))
output.close()
input_file.close()
