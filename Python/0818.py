input_file = open('INPUT.txt', 'r')
content = input_file.read().split()
box = [int(i) - 1 for i in content[1:]]
out = sum(box) + 1
output = open('OUTPUT.txt', 'w')
output.write(str(out))
output.close()
input_file.close()
