input_file = open('INPUT.txt', 'r')
content = input_file.read().split()

output = open('OUTPUT.txt', 'w')
output.write(str(out))
output.close()
input_file.close()
