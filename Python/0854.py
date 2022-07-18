input_file = open('INPUT.txt', 'r')
content = input_file.read().split()
box = [int(i) for i in content[0:2]]
min1 = min(box)
max1 = max(box)
if content[2] == "heat":
    out = max1
elif content[2] == "freeze":
    out = min1
elif content[2] == "auto":
    out = box[1]
elif content[2] == "fan":
    out = box[0]
output = open('OUTPUT.txt', 'w')
output.write(str(out))
output.close()
input_file.close()
