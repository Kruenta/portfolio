input_file = open('INPUT.txt', 'r')
content = input_file.read().split()
number = int(content[0])
output = open('OUTPUT.txt', 'w')
output.write(content[1][0:number-1] + content[1][number:])
output.close()
input_file.close()
