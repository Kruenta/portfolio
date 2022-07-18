input_file = open('INPUT.txt', 'r')
content = input_file.read().split("\n")
a = content[1].split()
out = ""
if int(content[2]) != 0:
    for i in content[3:]:
        indexes = [int(j) for j in i.split()]
        out = out + " ".join(a[indexes[0] - 1:indexes[1]]) + "\n"
output = open('OUTPUT.txt', 'w')
output.write(out.rstrip())
output.close()
input_file.close()
