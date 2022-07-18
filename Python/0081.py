input_file = open('INPUT.txt', 'r')
content = input_file.read().split()
box = [int(i) for i in content[1:]]
teta = min(box)
me = max(box)
output = open('OUTPUT.txt', 'w')
output.write(str(teta) + " " + str(me))
output.close()
input_file.close()
