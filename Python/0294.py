input_file = open('INPUT.txt', 'r')  # 0943 0062
content = input_file.read().split()
box = [int(i) for i in content]
proebanabolt = box[0] * (box[1] / 100)
proebanagayka = box[3] * (box[4] / 100)
bolt = box[0] - proebanabolt
gayka = box[3] - proebanagayka
diff = abs(gayka - bolt)
if box[3] > box[0]:
    out = (proebanabolt * box[2]) + (proebanagayka * box[5]) + diff * box[5]
else:
    out = (proebanabolt * box[2]) + (proebanagayka * box[5]) + diff * box[2]
output = open('OUTPUT.txt', 'w')
output.write(str(int(out)))
output.close()
input_file.close()
