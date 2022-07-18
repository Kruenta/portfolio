input_file = open('INPUT.txt', 'r')
content = input_file.read().split()
home = max([(i + 1, x) for i, x in enumerate(content[1:]) if x.split()[1] == '1'],
           key=lambda x: (int(x[1].split()[0])),
           default=['-1'])
output = open('OUTPUT.txt', 'w')
output.write(str(home))
output.close()
input_file.close()
