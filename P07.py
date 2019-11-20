import datetime

date_s = datetime.datetime(1966, 7, 13)
date_e = datetime.datetime(2020, 7, 24)
diff = (date_e - date_s).days
for i in range(diff):
    YYYYMMDD = "{:4}{:02}{:02}".format(date_s.year,date_s.month,date_s.day)
    bin_s = str(bin(int(YYYYMMDD)).split('b')[1])
    if bin_s == bin_s[::-1] :
        print(YYYYMMDD)
    date_s += datetime.timedelta(days=1)
