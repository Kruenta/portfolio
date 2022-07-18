input_file = open('INPUT.txt', 'r')
content = input_file.read().split()
box = [int(i) for i in content[1:]]
out = 0
max = 0
for i in box:
    if i > 0:
        out = out + 1
        if max < out:
            max = out
    else:
        out = 0
output = open('OUTPUT.txt', 'w')
output.write(str(max))
output.close()
input_file.close()
