input = open('INPUT.txt', 'r')
content = input.read().split()
sum = int(content[0]) - 1
sum1 =  int(content[1]) - 1
output = open('OUTPUT.txt', 'w')
output.write(str(sum1) + ' ' + str(sum))
output.close()
input.close()
