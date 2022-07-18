input_file = open('INPUT.txt', 'r')
content = input_file.read().split()
box = [int(x) for x in content]
box.sort()
if box[0] + box[1] > box[2] and box[2] + box[1] > box[0] and box[2] + box[0] > box[1]:
    out = "YES"
else:
    out = "NO"
output = open('OUTPUT.txt', 'w')
output.write(str(out))
output.close()
input_file.close()
