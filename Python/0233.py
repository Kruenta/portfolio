input_file = open('INPUT.txt', 'r')
content = input_file.read().split()[1:]
box = [int(x) for x in content]
count = 1
crash = False
for x in box:
    if x <= 437:
        crash = True
        break
    else:
        count += 1
if crash:
    out = "Crash " + str(count)
else:
    out = "No crash"
output = open('OUTPUT.txt', 'w')
output.write(str(out))
output.close()
input_file.close()
