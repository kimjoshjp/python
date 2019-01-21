#
#
#
#
# Def with unpacking param

モジュールを使う場合、import モジュールとすることで利用できるようになります。

import datetime
print(datetime.datetime.now())  # 現在時刻表示
from モジュール import 対象とすると、モジュール.対象の代わりに単に対象だけで使えるようになります。

from datetime import datetime
print(datetime.now())  # 現在時刻表示
記述量を減らしたい場合は、fromを使うとよいでしょう。

from datetime import datetime

now = datetime.now()
print(now.year, '/', now.month,'/', now.day, sep='')
print(now.hour,':', now.minute,':', now.second, sep='')


文字列・日時の変換はメソッド名がとても似ていて、混同しやすいので気をつけましょう。

str p time() : 文字列から日時への変換
文字列を指定したフォーマットで日時に変換します。

from datetime import datetime

day_str = '2018/3/14 12:30:00'
dt = datetime.strptime(day_str, '%Y/%m/%d %H:%M:%S') # 第二引数には変換したい文字列に一致したフォーマットを渡す
print(dt) # 2018-03-14 12:30:00
str f time() : 日時から文字列への変換
日時を指定したフォーマットの文字列に変換します。

from datetime import datetime

day = datetime(2018, 3, 14, 12, 30, 00) # 2018年3月14日 12:30:00

day_str = day.strftime('%Y/%m/%d') # YYYY/mm/ddのフォーマットの文字列に変換
print(day_str) # 2018/03/14


