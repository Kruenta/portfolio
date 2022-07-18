input = open('INPUT.txt', 'r')
content = input.read().split()[1:]
content.reverse()
k = ' '.join(content)
output = open('OUTPUT.txt', 'w')
output.write(k)
output.close()
input.close()
