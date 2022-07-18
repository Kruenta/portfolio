input_file = open('INPUT.txt', 'r')  # 0052
content = input_file.read().split()
out = ""
for bilet in content[1:]:
    biletleft = sum([int(x) for x in bilet[0:3]])
    biletright = int("".join(bilet[3:]))  #
    biletright1 = sum([int(x) for x in str(biletright + 1)])
    biletright2 = sum([int(x) for x in str(biletright - 1)])
    if biletleft == biletright1 or biletleft == biletright2:
        out = out + 'Yes\n'
    else:
        out = out + "No\n"
output = open('OUTPUT.txt', 'w')
output.write(str(out))
output.close()
input_file.close()
