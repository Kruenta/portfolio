import datetime
input_file = open('INPUT.txt', 'r')
content = input_file.read().split()
dt = content[0].split(":")
time = datetime.datetime(2001, 3, 5, int(dt[0]), int(dt[1]))
time = time + datetime.timedelta(hours=int(content[1]), minutes=int(content[2]))
output = open('OUTPUT.txt', 'w')
output.write(time.strftime("%H:%M"))
output.close()
input_file.close()
