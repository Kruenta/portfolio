input_file = open('INPUT.txt', 'r')
content = input_file.read().split()
prices = [int(i) for i in content[0:3]]
bank = [int(k) for k in content[3:]]
prices.sort()
bank.sort()
multiplied = [a * b for a, b in zip(prices, bank)]
s = sum(multiplied)
output = open('OUTPUT.txt', 'w')
output.write(str(s))
output.close()
input_file.close()
