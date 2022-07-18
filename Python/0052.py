input_file = open('INPUT.txt', 'r')
content = input_file.read().zfill(6)
if sum([int(x) for x in content[0:3]]) == sum([int(x) for x in content[3:]]):
    out = 'YES'
else:
    out = "NO"
output = open('OUTPUT.txt', 'w')
output.write(out)
output.close()
input_file.close()
