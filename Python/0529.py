import math

input_file = open('INPUT.txt', 'r')
content = input_file.read().split()
box = [int(x) for x in content]
sum = round(math.sqrt(((box[0]-box[2]) ** 2) + ((box[1]-box[3]) ** 2)), 5)
output = open('OUTPUT.txt', 'w')
output.write(str(sum))
output.close()
input_file.close()
