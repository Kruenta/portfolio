input = open('INPUT.txt', 'r')
content = int(input.read())
if content == 12 or content == 1 or content == 2:
    out = "Winter"
elif content == 9 or content == 10 or content == 11:
    out = "Autumn"
elif content == 6 or content == 7 or content == 8:
    out = "Summer"
elif content == 3 or content == 4 or content == 5:
    out = "Spring"
else:
    out = "Error"
output = open('OUTPUT.txt', 'w')
output.write(out)
output.close()
input.close()
