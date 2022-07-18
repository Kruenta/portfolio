input_file = open('INPUT.txt', 'r')  # 0943 0062
content = input_file.read().split()
kletkaA = int(content[0]) + int(content[1])
kletkaB = int(content[2]) + int(content[3])
black = [i for i in range(1, 65) if i % 2 == 0]
white = [i for i in range(65) if i % 2 != 0]
if kletkaA in black and kletkaB in black:
    out = "YES"
elif kletkaA in white and kletkaB in white:
    out = "YES"
else:
    out = "NO"
output = open('OUTPUT.txt', 'w')
output.write(str(out))
output.close()
input_file.close()
