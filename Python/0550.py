input_file = open('INPUT.txt', 'r')
content = int(input_file.read())
if (content % 4 == 0 and content % 100 != 0) or content % 400 == 0:
    day = "12"
else:
    day = "13"
output = open('OUTPUT.txt', 'w')
output.write(day + "/09/" + str(content).zfill(4))
output.close()
input_file.close()
