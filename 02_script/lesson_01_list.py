"""
■リスト内包表記
・基本
[式 for 任意の変数名 in イテラブルオブジェクト]

・条件式を追加することも可能(Trueとなる要素のみ追加される)
[式 for 任意の変数名 in イテラブルオブジェクト if 条件式]

・三項演算子と組み合わせる
[真のときの値 if 条件式 else 偽のときの値 for 任意の変数名 in イテラブルオブジェクト]
"""

# まずは処理時間を比較
import time


start = time.time()

# for文の場合
sample_list = []
for number in range(100000000):
    sample_list.append(number)

stop = time.time()
result = stop - start
print(f'for文の処理時間 : {round(result, 4)}')


start = time.time()

# リスト内包表記の場合
sample_list = [number for number in range(100000000)]

stop = time.time()
result = stop - start
print(f'内包表記の処理時間 : {round(result, 4)}')



# ワーク1 : 内包表記を用いて[0, 1, 2, 3   , 4]となるリストを作成しよう


# ワーク2 : 内包表記と条件式を用いて[4, 16, 36, 64]となるリストを作成しよう


# ワーク3 : 内包表記と三項演算子を用いて偶数の場合は'偶数' 奇数の場合は'奇数'となる0から9のリストを作成しよう
