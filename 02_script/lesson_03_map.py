"""
■ビルドイン関数 : map
・基本
map(callable, *iterable)

・厳密には違うが汎用的な例で書くとこうなる
map(function, list)

・iterableなオブジェクトはいろいろある
tuple
dict
str
ジェネレータ式(イテレータ)
mapオブジェクト(イテレータ)
fileオブジェクト(イテレータ)
"""


# MEMO : mapはmap型を返す
numbers = map(int, ["1", "2", "3", "4", "5"])
what_type_is_numbers = type(numbers)
# <class 'map'>

# MEMO : map型 -> list型にしてあげる
numbers = list(map(int, ["1", "2", "3", "4", "5"]))
what_type_is_numbers = type(numbers)
# <class 'list'>


# MEMO : 自作の関数をmapのcallableに割り当てる
def capitalize(word):
    return word.capitalize()

words = ["january", "february", "march", "april", "may", "june"]
capitalize_words = list(map(capitalize, words))


# MEMO : mapに複数の引数を渡す
def multiple(x, y):
    return x*y

args_x = [1, 2, 3, 4, 5]
args_y = [3, 4, 5, 6, 7]
result = list(map(multiple, args_x, args_y))
# [3, 8, 15, 24, 35]


# ワーク1 : 以下のリストに対してmapを使って絶対値を求めてみよう  ヒント:abs()
absolute_values = [3, -14, -5 , 1, -6]


# ワーク2 : リストの要素を真偽値(bool型)に変換して格納しよう
bool_lists = [0, 1, -1, False, 'False']