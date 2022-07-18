input_file = open('INPUT.txt', 'r')  # 0854 0504 0062
content = input_file.read()
number = [True, False, False]
for i in content:
    if i == "A":
        box = number[1]
        number[1] = number[0]
        number[0] = box
    if i == "B":
        box = number[2]
        number[2] = number[1]
        number[1] = box
    if i == "C":
        box = number[2]
        number[2] = number[0]
        number[0] = box

out = number.index(True) + 1
output = open('OUTPUT.txt', 'w')
output.write(str(out))
output.close()
input_file.close()
