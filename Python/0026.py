import math
input_file = open('INPUT.txt', 'r')  # 0943 0062
content = input_file.read().split()
box = [int(i) for i in content]
r = math.sqrt((box[3] - box[0])**2 + (box[4] - box[1])**2)
if r <= box[2] + box[5] and box[2] + r >= box[5] and box[5] + r >= box[2]:
    out = "YES"
else:
    out = "NO"
output = open('OUTPUT.txt', 'w')
output.write(str(out))
output.close()
input_file.close()
