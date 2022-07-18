input_file = open('INPUT.txt', 'r')
content = input_file.read().split()
m, n = int(content[1]), int(content[0])
matrix = [[i + m * j for i in range(m)][::pow(-1, j)] for j in range(n)]
output = open('OUTPUT.txt', 'w')
output.write(str(matrix[int(content[2]) - 1][int(content[3]) - 1]))
output.close()
input_file.close()
