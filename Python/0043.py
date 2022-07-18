input_file = open('INPUT.txt', 'r')  # 0052
content = input_file.read()
out = 0
max = 0
for i in content:
    if i == "0":
        out = out + 1
        if max < out:
            max = out
    else:
        out = 0
output = open('OUTPUT.txt', 'w')
output.write(str(max))
output.close()
input_file.close()
