

# 問題文では import random とモジュールを呼び出していたので、関数を利用する場合に num_randint = random.randint(1, 100) と モジュール名.関数名 と呼び出していました。
# 呼び出し時に from モジュール名 import 関数名 と書くと関数名のみで利用できます。


from random import randint, choice



numbers = [199, 288, 56, 82, 99, 1, 538, 499]

num_randint = randint(1,100)
print(num_randint)

num_choice = choice(numbers)
print(num_choice)

#### Q2

def div_and_mod(x,y):
    div = x // y
    mod = x % y
    return div, mod

div1, mod1 = div_and_mod(100, 23)
print(div1, mod1)

div2, mod2 = div_and_mod(235, 17)
print(div2, mod2)

result3 = div_and_mod(235, 17)
print(result3)

x = divmod(10,3)
print(x)
print(x[0],x[1])

