#
#
#
# -*- conding : utf-8 -*-

apple_price = 200;
money = 1000;

input_count = input('Please input number of apple:')
count = int(input_count)
total_price = apple_price * count
zankin = money - total_price

print('total number' + str(count) + 'desu')
print('支払い金額は' + str(total_price) + '円です')

# moneyとtotal_priceの比較結果によって条件を分岐してください

if money > total_price:
    print ('りんごを'+str(count)+'個買いました')
    print ('残金は'+str(zankin)+'円です')

elif money == total_price:
    print ('りんごを'+str(count)+'個買いました')
    print ('財布が空になりました')

else: 
    print ('お金が足りません')
    print ('りんごを買えませんでした')
    