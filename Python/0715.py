input_file = open('INPUT.txt', 'r')
content = input_file.read().split("\n")
a = content[0].split()
lange = int(a[0]) + 1
origin = content[1:lange]
invert = content[lange + 1:]
dictionary = {
    "W": "B",
    "B": "W"
}
errors = 0
for x, y in zip(origin, invert):
    for i in range(0, int(a[1])):
        if dictionary[x[i]] != y[i]:
            errors += 1
output = open('OUTPUT.txt', 'w')
output.write(str(errors))
output.close()
input_file.close()
