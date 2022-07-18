input = open('INPUT.txt', 'r')
content = input.read().split()
sum = int(content[0]) + int(content[2]) + int(content[4]) + int(content[6])
sum1 = int(content[1]) + int(content[3]) + int(content[5]) + int(content[7])
if sum < sum1:
    out = "2"
elif  sum > sum1:
    out = "1"
else:
    out = "DRAW"
output = open('OUTPUT.txt', 'w')
output.write(out)
output.close()
input.close()

first = sum([int(x) for idx, x in content if idx%2 == 0])
second = sum([int(x) for idx, x in content if idx%2 != 0])
