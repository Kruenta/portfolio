input = open('INPUT.txt', 'r')
content = input.read().split()
content = [int(i) for i in content]
content.sort()
out = str(content[-1] - content[0])
output = open('OUTPUT.txt', 'w')
output.write(out)
output.close()
input.close()
