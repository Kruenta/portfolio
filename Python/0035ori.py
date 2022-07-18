input_file = open('INPUT.txt', 'r')
content = input_file.read().split()
key = [int(x) for x in content[1:]]
print(key[0])
m = [x for idx, x in key if idx % 2 == 0]
n = [x for idx, x in key if idx % 2 != 0]
out = [int(19 * mi + (ni + 239) * (ni + 366) / 2) for mi, ni in zip(m, n)]
out = "\n".join(out)
output = open('OUTPUT.txt', 'w')
output.write(out)
output.close()
input_file.close()
