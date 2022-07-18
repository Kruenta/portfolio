input_file = open('INPUT.txt', 'r')
content = input_file.read().split()
content = [int(i) for i in content[1:]]
content.append(content[0])
content.insert(0, content[-2])
out = []
for i in range(1, len(content)-1):
    out.append(content[i] + content[i-1] + content[i+1])
output = open('OUTPUT.txt', 'w')
output.write(str(max(out)))
output.close()
input_file.close()
