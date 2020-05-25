#
#
#


with open('input/lunch.csv',encoding='utf-8') as f:
    menu = f.read()
    print(menu)

文字列.rstrip() メソッドを用いると行の最後の改行を削除します。

文字列.rstrip() メソッドは文字列の末尾部分に存在する 空白 、 タブ 、 改行 などを取り去ります。

他には文字列の両脇の空白などを削除する 文字列.strip() メソッド、文字列の先頭部分の空白などを削除する 文字列.lstrip() メソッドがあります。

公式ドキュメント
以下は公式ドキュメントへのリンクです。

str.rstrip()
str.lstrip()
str.strip()

num_string = '100 200 300 400 500'

nums = num_string.split(' ')

for x in nums:
    print(x)

sample = 'a,b,c,d,e'
print (type(sample))
sample_list = sample.split(',')

print(sample_list)
print(type(sample_list))

with open('input/menu.csv', encoding='utf-8') as f:
    for row in f:
        row_string = row.rstrip()
        columns = row_string.split(',')
        name = columns[0]
        price = columns[1]
        print(name + 'は' + price + '円')

文字列の .split() メソッドを使って、メニューファイルの各行のデータを分解しました。
各行はカンマ区切りの文字列なので、 row_string.split(',') を使って文字列のリスト columns に変換しています。

columns は以下のようなリストになります。

columns = ["のり弁当", "350"]
この columns リストから columns[0] や columns[1] のように値（メニュー名と価格）を取り出しています。

name = columns[0]
price = columns[1]
今回のプログラムでは各行を分解する処理で、以下のように rstrip 、 split を分けた2行で書いています。

   row_string = row.rstrip()
   columns = row_string.split(',')
上記は、以下のように1行で書けます。

    columns = row.rstrip().split(',')
こうすると 元の行（文字列） => 末尾の改行を消した行（文字列） => カンマで区切ったリスト と一気に処理できます。

with open('input/menu.csv', encoding='utf-8') as f:
    for row in f:
        columns = row.rstrip().split(',')
        name = columns[0]
        price = columns[1]
        print(name + 'は' + price + '円')


with open('input/telephone.csv', encoding='utf-8') as f:
    for row in f:
        columns = row.rstrip().split(',')
        day_of_week = columns[0]
        in_charge = columns[1]

        # 表示
        print(day_of_week + 'は' + in_charge + 'さんです。')


ヒント
変数 name が’うな重'か、'ビビンバ丼'の場合だけ価格から100円を引きます

以下の例は変数 str_sample が a 、 b 、 c の場合のみ文字列が表示されます。

str_sample = 'a'
# 判定
if str_sample in ['a', 'b', 'c']:
    print(str_sample + 'が含まれます')

print('<<丼100円引きデー>>')
with open('input/menu.csv', encoding='utf-8') as f:
    for row in f:
        columns = row.rstrip().split(',')
        name = columns[0]
        price = int(columns[1])
        # 100円引きの計算
        if name in ['うな重','ビビンバ丼']:
            discount = int(price - 100)
            print(name, ':', discount, '円', sep='')
        else:
            print(name, ':', price, '円', sep='')


orders = {}  # この行は直さないでください

# ファイルinput/lunch.csvを開いて、集計
with open ('input/lunch.csv', encoding='utf-8') as f:
    for row in f:
        conv_list = row.rstrip().split(',')
        order = conv_list[1]
        
        if order in orders:
            orders[order] +=1
            
        else:
            orders[order] =1
        
        

for menu_name, count in orders.items():
    print(menu_name + ':' + str(count))
