input_file = open('INPUT.txt', 'r')
content = input_file.read()
out = (int(content) * int(content)) - ((int(content) - 1) * 3) - 1
output = open('OUTPUT.txt', 'w')
output.write(str(out))
output.close()
input_file.close()
