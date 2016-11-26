import datetime


t = datetime.datetime.now()
time_var = str(t.month) + str(t.day) + str(t.hour) + str(t.minute) + str(t.second)


fin = open("testdata.txt")
fout = open("outputtest" + time_var + ".txt", 'w')


for row in fin:
    row = r'"' + row
    row = row.replace('\t', r'","')
    fout.write(row)
