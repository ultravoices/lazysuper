import os
from datetime import datetime

raw_filename = input("Filename of FHATWOA output in ACLIOUT? ")
FILENAME = os.path.join("V:", raw_filename)

fin = open(FILENAME)
count = 0
error_count = 0
today_date = datetime.now()  # TODO allow for selecting batch date

for line in fin:
    count += 1
    if not line.startswith(r"2A "):  # blocks that start with 2A and a space are format 1
        block_id_number = line[76:80]
        block_id_number_numeric = int(line[76:80])
        misc_code = int(line[22:24])
        line_credit_month = line[43:45]
        line_credit_day = line[45:47]
        line_credit_year = "20" + line[47:49]
        formatted_date_line = datetime(int(line_credit_year), int(line_credit_month), int(line_credit_day))
        delta = datetime.now() - formatted_date_line  # subtracting gives a timedelta object
        if delta.days > 20 and line[24] is not "6":   # taking the days method extracts timedelta as an int
            print("missing 6 error on record ", count, " block ", block_id_number, "it is", delta.days, "days")
            error_count += 1
        if delta.days <= 20 and line[24] is "6":
            print("extra 6 error on record", count, "block", block_id_number, "it is", delta.days, "days")
            error_count += 1
        if block_id_number_numeric >= 9000:  # white blocks are 9000-9099
            if block_id_number_numeric <= 9099:
                if misc_code != 0:
                    print("white block", block_id_number, "record", count, "is not 00")
                    error_count += 1
        if block_id_number_numeric >= 9100:  # blue blocks are 9100-9299 or 9300-9479
            if block_id_number_numeric <= 9479:
                if misc_code == 0:
                    print("blue block", block_id_number, "record", count, "is 00")
                    error_count += 1

print("error count:", error_count)

fin.close()
