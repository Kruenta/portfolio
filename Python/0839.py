input_file = open('INPUT.txt', 'r')
content = input_file.read()
if "0" in content:
    out = "NO"
else:
    out = "YES"
output = open('OUTPUT.txt', 'w')
output.write(str(out))
output.close()
input_file.close()
