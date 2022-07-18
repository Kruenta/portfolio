input = open('INPUT.txt', 'r')
content = input.read()
nums = [2 ** n for n in range(0, 30)]
print(nums)
if int(content) in nums:
    out = "YES"
else:
    out = "NO"
output = open('OUTPUT.txt', 'w')
output.write(out)
output.close()
input.close()
