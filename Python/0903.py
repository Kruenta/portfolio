input = open('INPUT.txt', 'r')
content = input.read()
sum = int(content) + 1 
output = open('OUTPUT.txt', 'w')
output.write(str(sum))
output.close()
input.close()
