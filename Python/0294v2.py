input_file = open('INPUT.txt', 'r')  # 0943 0062
content = input_file.read().split()
k1, l1, m1, k2, l2, m2 = [int(i) for i in content]
a = (k1 * l1) / 100
a1 = (k2 * l2) / 100
s = a * m1 + a1 * m2
r1 = k1 - a
r2 = k2 - a1
if r1 > r2:
    s += (r1 - r2) * m1
else:
    s += (r2 - r1) * m2
output = open('OUTPUT.txt', 'w')
output.write(str(int(s)))
output.close()
input_file.close()
