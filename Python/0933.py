input_file = open('INPUT.txt', 'r')
content = input_file.read().split()
box = [int(x) for x in content]
if box[0] >= box[3]:
    out = (box[3] * box[1])
else:
    out = (box[3] - box[0]) * box[2] + box[0] * box[1]
output = open('OUTPUT.txt', 'w')
output.write(str(out))
output.close()
input_file.close()
