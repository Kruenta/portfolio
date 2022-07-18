from math import ceil

input_file = open('INPUT.txt', 'r')
content = input_file.read().split()
box = [int(x) for x in content]
sum = ceil(((box[0] * 2) + (box[1] * 2)) * box[2] / 16)
output = open('OUTPUT.txt', 'w')
output.write(str(sum))
output.close()
input_file.close()
