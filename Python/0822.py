input_file = open('INPUT.txt', 'r')  # 0529
content = input_file.read().split()
box = [int(i) for i in content]
sum = ((box[0] - box[4]) * (box[3] - box[5]))
sum1 = ((box[2] - box[4]) * (box[1] - box[5]))
out = (sum - sum1) * 0.5
output = open('OUTPUT.txt', 'w')
output.write(str(abs(out)))
output.close()
input_file.close()
