input = open('INPUT.txt', 'r')
content = input.read().split()
sum = int(content[0]) * int(content[1]) + int(content[0]) * int(content[2]) + int(content[1]) * int(content[2])
sum1 = 2 * sum
sum2 = int(content[0]) * int(content[1]) * int(content[2])
output = open('OUTPUT.txt', 'w')
output.write(str(sum1) + " " + str(sum2))
output.close()
input.close()