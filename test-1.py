#
#
#
#

comp_list = [y for y in range(10)]
print(comp_list)

def multiplication(a, b):
    """ 掛け算をする関数 """
    if a == 0 or b == 0:
        raise ValueError("引数のどちらか、あるいは両方がゼロになっています")
    return a * b

answer = multiplication(10, 8) # 正常終了
print(answer)
try:
    answer = multiplication(10, 0) # 例外発生
    print(answer)

#except ValueError as e:
#    print(e.args)