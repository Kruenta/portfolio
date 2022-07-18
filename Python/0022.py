input_file = open('INPUT.txt', 'r')  # 0052
content = input_file.read()
s = 0
while int(content) > 0:
    s = s + int(content) % 2
    content = int(content) // 2
print(s, content)
output = open('OUTPUT.txt', 'w')
output.write(str(s))
output.close()
input_file.close()
