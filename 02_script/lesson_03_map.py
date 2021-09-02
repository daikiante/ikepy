"""
■ビルドイン関数 : map
・基本
map(callable, *iterable)

・厳密には違うが分かりやすく書くとこうなる
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