input_file = open('INPUT.txt', 'r')
content = input_file.read()
a = ["G", "C", "V"]
for i in range(0, int(content)):
    last = a[2]
    a[2] = a[1]
    a[1] = a[0]
    a[0] = last
output = open('OUTPUT.txt', 'w')
output.write("".join(a))
output.close()
input_file.close()
