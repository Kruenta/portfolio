input_file = open('INPUT.txt', 'r')
content = input_file.read().split()
box = [int(i) for i in content]
out = []
for i in range(-100, 101):
    if box[0] * i * i * i + box[1] * i * i + box[2] * i + box[3] == 0:
        out.append(str(i))


output = open('OUTPUT.txt', 'w')
output.write(" ".join(out))
output.close()
input_file.close()
