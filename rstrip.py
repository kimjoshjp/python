#
#
#
#
#

import pandas as pd

'''
aLdata = []

with open ('sales.csv') as f:
    for row in f:
        row_string = row.rstrip()

        aLdata.append(row_string)

print(aLdata)
'''

df = pd.read_csv('sales.csv')
print(df)