#
#
#
#
d = {'k1':1, 'k2':2, 'k3':3}
d['k0']= d['k1']
del d['k1']

print(d)


#1から10の間などの範囲を条件で判定する場合、
#変数を挟んで条件（より小さい、より大きい、以上、以下）を指定できます。

if 1 <= x <= 10:
    print('1以上、10以下')

#
#辞書に値を追加するには辞書名[キー] = 値と書きます。
#すでに値が存在していても、辞書名[キー] = "新しい値"で値を上書きできます。
#辞書のdel文（del 辞書名[キー]）は削除した値を利用できません。1要素を削除します。

#in演算子を利用し、辞書に特定のキーを持つ要素が存在するか確認できます。

if "キー" in 辞書:と指定すると、辞書の部分がキーのリストのときと同一の判定をします。

下の例では、if '体脂肪' in ['名前', '年齢', '身長', '体重', '視力']:と同じ判定をします。

辞書.keys()は辞書に存在するキーの一覧を返します。dict_keys()で囲まれていますが、リストと同じようにfor文などで利用できます。
list()で囲めば、リストに変換できます。

辞書.keys()は辞書に存在するキーの一覧を返します。dict_keys()で囲まれていますが、リストと同じようにfor文などで利用できます。
list()で囲めば、リストに変換できます。

health_result = {'名前': '佐藤', '年齢': 35, '身長': 170, '体重': 60, '視力': 2.0}

keys = list(health_result.keys())

print(keys)

for key in keys:
    print(key)
実行結果:

['名前', '年齢', '身長', '体重', '視力']
名前
年齢
身長
体重
視力

health_result = {'名前': '佐藤', '年齢': 35, '身長': 170, '体重': 60, '視力': 2.0}

# 値のリストを表示
health_result_values = health_result.values()
# 表示
print(health_result_values)

health_result = {'名前': '佐藤', '年齢': 35, '身長': 170, '体重': 60, '視力': 2.0}

# 値のリストを表示
health_result_values = list(health_result.values())

# 表示
print(health_result_values)

辞書.items()は辞書のキーと値の(key, value)対のリストを返します。
dict_items()で囲まれていますが、リストと同じようにfor文などで利用できます。
list()で囲めば、リストに変換できます。

for文でforの後ろに変数をカンマ区切りで2つ指定すると、辞書のキーが1番目、値が2番目の変数に代入されます。

health_result = {'名前': '佐藤', '年齢': 35, '身長': 170, '体重': 60, '視力': 2.0}

items = list(health_result.items())

print(items)

for key, item in items:
    print(key, item)

dc = {'パンダ': '1-1', '象': '2-1', '猿': '2-2'}

for key in dc:
    print(key,dc[key])
    print(dc[key])


for 変数 in 辞書という書き方はシンプルですが、キーのみ取得できます。
forの中で値を使う場合は、辞書[変数]が必要になります。この書き方は効率が悪いので、itemsを使うようにしましょう。

items = {'ボールペン': 12,
         'ノート': 3,
         'のり': 5}

tel = ['ノート', 'のり', 'ボールペン', 'のり']

for item in tel:
    print(item, items[item])


# 文房具ごとの在庫数
items = {'ボールペン': 12,
         'ノート': 3,
         'のり': 5}

item = 'ボールペン'

#リストitemsのボールペンを　-5 
items[item] -= 5

for item,num in items.items():
    print(item,num)

items[item]は最初12本でした。
items[item] -= 5とすることで、辞書の値を更新できます。
全ての在庫を表示すると、ボールペンの在庫が7本になっているのを確認できます。

同じようにin演算子で文字列に特定の文字列が含まれるかを確認できます。

zen = "Beautiful is better than ugly."

if 'better' in zen:
    print('"better" is included!')

実は、if 'ノート' in stationery_dict: と if 'ノート' in stationery_dict.keys(): は同じ結果です。

辞書に特定のキーが含まれるか調査する場合は、 if 特定のキー in 辞書: を利用します。

あまり使いませんが、辞書に特定の値が含まれているか調査する場合は、 辞書.values() を利用します。

fruits = {'Apple': 'リンゴ',
          'Orange': 'ミカン',
          'Grapes': 'ブドウ'}

if 'ブドウ' in fruits.values():
    print('ブドウは含まれています。')

stationery_dict = {'ボールペン': 0,
                   'ノート': 0,
                   'のり': 0}

# 各値を1増加
stationery_dict['ボールペン'] += 1
stationery_dict['ノート'] +=1
stationery_dict['のり'] +=1


used = ['ボールペン', 'ノート', 'のり', 'のり', 'ノート']

# 集計用辞書
stationery_dict = {'ボールペン': 0,
                   'ノート': 0,
                   'のり': 0}

# 各文房具の利用回数の計算
for use in used:
    stationery_dict[use] +=1
    
# 結果の表示
print(stationery_dict)


# 辞書fruits作成
fruits = {'Apple': 'リンゴ', 'Orange': 'ミカン', 'Grapes': 'ブドウ'}

# 確認用リスト
check_list = ['Apple', 'Peach', 'Grapes']

for key in check_list:
    if key in fruits:
        print(fruits[key], 'は存在します。', sep='')


used = ['ボールペン', 'ノート', 'のり', 'のり', 'ノート']

# 集計用辞書
items = {}

# 各文房具の利用回数の計算
for name in used:
    if name in items:
        items[name] +=1
    else:
        items[name] =1
    
# 結果の表示
print(items)

# 利用状況
used = ['ボールペン', 'ノート', 'のり', 'のり', 'ノート']

# 集計用辞書
items = {}

# 各文房具の利用回数の計算
for name in used:
    if name in items:
        items[name] +=1
    else:
        items[name] =1
    
# 結果の表示
print(items)


egetables = ['大根', '人参', 'じゃがいも', 'じゃがいも', '人参', 'じゃがいも']

# 集計用辞書
veg_counts = {}

# 野菜の数を集計
for vegs in vegetables:
    if vegs in veg_counts:
        veg_counts[vegs] +=1
    
    else:
        veg_counts[vegs] =1
        
# 結果の表示
print(veg_counts)