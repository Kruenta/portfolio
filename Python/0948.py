from math import ceil

input_file = open('INPUT.txt', 'r')
content = input_file.read().split()
total_string = int(content[0])
string_number = int(content[1])
book_list = ceil(string_number / total_string)
string_number = string_number - ((book_list - 1) * total_string)
output = open('OUTPUT.txt', 'w')
output.write(str(book_list) + " " + str(string_number))
output.close()
input_file.close()
