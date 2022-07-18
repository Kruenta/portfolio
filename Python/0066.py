input_file = open('INPUT.txt', 'r')
content = input_file.read()
string = "qwertyuiopasdfghjklzxcvbnmq"
if content == "m":
    out = "q"
else:
    k = string.index(content) + 1
    out = string[k]
output = open('OUTPUT.txt', 'w')
output.write(out)
output.close()
input_file.close()
