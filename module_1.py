#
#
#
#
# 

from datetime import datetime

with open('days.txt', encoding='utf-8') as f:
    for row in f:
        str_row = row.rstrip()
        str_row = datetime.strptime(str_row, '%Y-%m-%d')
        str_row = datetime.strftime(str_row, '%Y/%m/%d')
        print(str_row)