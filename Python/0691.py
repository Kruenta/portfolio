import re

input_file = open('INPUT.txt', 'r')
content = input_file.read().split()
out = ""
for i in content[1:]:
    if re.match(r'[ABCEHKMOPTXY]{1}\d{3}[ABCEHKMOPTXY]{2}', i) is not None and len(i) == 6:
        out = out + "Yes\n"
    else:
        out = out + "No\n"
output = open('OUTPUT.txt', 'w')
output.write(str(out))
output.close()
input_file.close()
