input = open('INPUT.txt', 'r')
content = int(input.read())
sum = content * content
output = open('OUTPUT.txt', 'w')
output.write(str(sum))
output.close()
input.close()
