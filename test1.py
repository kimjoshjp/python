#
#
#
"""
book_user = []

# 表示
with open('input/room.csv', encoding='utf-8') as f:
    for row in f:
        columns = row.rstrip().split(',')
        room = columns[0]
        name = columns[1]
        
        if '会議室A' ==room:
            if name not in book_user:
                book_user.append(name)
            
print(book_user)
"""


stationery = {}
stationery['ボールペン'] = 22
stationery['ノート'] = 31
stationery['のり'] = 8

total = 0
for sum in stationery.values():
    total += sum
print(total)