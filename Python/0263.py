input_file = open('INPUT.txt', 'r')  # 0052
content = input_file.read().split()
metro = abs(int(content[1]) - int(content[2])) - 1
if metro >= int(content[0]) // 2:
    metro = int(content[0]) - metro - 2
output = open('OUTPUT.txt', 'w')
output.write(str(metro))
output.close()
input_file.close()
