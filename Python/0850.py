input_file = open('INPUT.txt', 'r')  # 0529
content = input_file.read().split()
box = [int(i) for i in content]
boxmax = (max(box) + 1) // 2
boxmin = min(box)
output = open('OUTPUT.txt', 'w')
output.write(str(boxmax) + " " + str(boxmin))
output.close()
input_file.close()
