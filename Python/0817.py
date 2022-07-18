input_file = open('INPUT.txt', 'r')  # 0943 0062
content = input_file.read().split()
box = [int(i) for i in content]
w = box[2] * box[2]
c = box[1] * box[0]
x = box[1] * (box[2] * box[3] - box[0] * w)
y = box[0] * (box[2] * box[3] - box[1] * w)
out = x + y + c * w
output = open('OUTPUT.txt', 'w')
output.write(str(int(out)))
output.close()
input_file.close()
