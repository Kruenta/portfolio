input = open('INPUT.txt', 'r')
content = input.read().split()
sum = int(content[0]) * int(content[1]) * int(content[2]) * 2
output = open('OUTPUT.txt', 'w')
output.write(str(sum))
output.close()
input.close()
