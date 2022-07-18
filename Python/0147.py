input_file = open('INPUT.txt', 'r')
content = input_file.read()

def fibonacci(content):
    a, b = 0, 1
    for i in range(int(content)):
        yield a
        a, b = b, a + b


data = list(fibonacci(int(content) + 1))
output = open('OUTPUT.txt', 'w')
output.write(str(data[-1]))
output.close()
input_file.close()
