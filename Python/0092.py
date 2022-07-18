input = open('INPUT.txt', 'r')
content = input.read()
kat = 2 * int(content) / 3
pet = int(content) / 6
ser = int(pet)
kat1 = int(kat)
pet1 = int(pet)
ser1 = int(ser)
output = open('OUTPUT.txt', 'w')
output.write(str(pet1) + ' ' + str(kat1) + ' ' + str(ser1))
output.close()
input.close()
