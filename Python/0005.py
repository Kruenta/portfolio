input_file = open('INPUT.txt', 'r')  # 0529
content = input_file.read().split()
box = [int(i) for i in content]
chet = []
nechet = []
for x in box[1:]:
    if x % 2 == 0:
        chet.append(x)
    else:
        nechet.append(x)
out = " ".join([str(f) for f in nechet]) + "\n"
out = out + " ".join([str(f) for f in chet]) + "\n"
if len(chet) >= len(nechet):
    out = out + "YES"
else:
    out = out + "NO"
output = open('OUTPUT.txt', 'w')
output.write(out)
output.close()
input_file.close()
