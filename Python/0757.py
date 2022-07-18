input_file = open('INPUT.txt', 'r')
content = input_file.read().split()
gen = [int(i) for i in content]
c = gen[0] // 2
h = gen[1] // 6
o = gen[2]
multiplied = [c, h, o]
out = min(multiplied)
output = open('OUTPUT.txt', 'w')
output.write(str(out))
output.close()
input_file.close()
