#
#
#
#
#
"""品目の集計."""

count = {}

with open('input/report.csv', encoding='utf-8') as f:
    for line in f:
        date, item_name, amount= line.rstrip().split(',')
        
        if item_name not in count:
            count[item_name] = 0
        
        count[item_name] += 1
            
  
for key,value in count.items():
    print(key, ":", value, sep='')