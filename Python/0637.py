input_file = open('INPUT.txt', 'r')  # 0943 0062
content = input_file.read().split("\n")
out = 0
rooms = int(content[2])
for i in content[1].split():
    if int(i) > rooms:
        out = out + rooms
    else:
        out = out + int(i)
output = open('OUTPUT.txt', 'w')
output.write(str(out))
output.close()
input_file.close()
