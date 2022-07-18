input_file = open('INPUT.txt', 'r')  # 0052
content = input_file.read()
out = content.count("8") * 2
out = out + content.count("6")
out = out + content.count("9")
out = out + content.count("0")
output = open('OUTPUT.txt', 'w')
output.write(str(out))
output.close()
input_file.close()
