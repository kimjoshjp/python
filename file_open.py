#
#
#
#

'''
with open ('output.txt', 'x', encoding='utf8') as f:
    f.write('hello, world\n')

print('書き込み完了')
'''


#2

week_duty = ['月曜日は木田',
             '火曜日は西川',
             '水曜日は大村',
             '木曜日は岡田',
             '金曜日は中村']

with open('trash.txt', 'x', encoding='utf-8') as f:
    for item in week_duty:
        f.write(item +'\n')
    
print('書き込み完了')