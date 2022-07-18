input_file = open('INPUT.txt', 'r')
content = int(input_file.read())
max = content * 6
min = content // 6  # div это // в паскале
if content % 6 != 0:  # % это операция взятия остатка от деления
    min = min + 7 - (content % 6)  # mod это % в паскале
output = open('OUTPUT.txt', 'w')
output.write(str(min) + " " + str(max))
output.close()
input_file.close()
