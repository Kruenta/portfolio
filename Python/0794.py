input_file = open('INPUT.txt', 'r')  # 0148 0818
content = input_file.read().split()
box = [int(i) for i in content]
out = box[0] * (box[1] // box[2] + min([box[1], box[2] - 1]))
output = open('OUTPUT.txt', 'w')
output.write(str(out))
output.close()
input_file.close()
