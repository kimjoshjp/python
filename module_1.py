#
#
#
#
# 

#1)
'''
from datetime import datetime

with open('days.txt', encoding='utf-8') as f:
    for row in f:
        str_row = row.rstrip()
        str_row = datetime.strptime(str_row, '%Y-%m-%d')
        str_row = datetime.strftime(str_row, '%Y/%m/%d')
        print(str_row)
'''

#2)

from datetime import datetime
from datetime import timedelta

# 基準の日付
str_date = '2016-10-20'
# 文字列を日付へ変換
base_day = datetime.strptime(str_date, '%Y-%m-%d')

# 5日前の日付
before_5days = base_day - timedelta(days=5)
# ファイルinput/days.txtを開く
with open('days.txt', encoding='utf-8') as f:
    for row in f:
        # 文字列を日付へ変換
        day = row.rstrip()
        day = datetime.strptime(day,'%Y-%m-%d')
        # 日付を比較
        if before_5days <= day < base_day:
            print (day.strftime('%Y/%m/%d'))

