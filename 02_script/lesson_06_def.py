"""
■型を明示的に定義する

Python3.5からType Hintsという機能が導入されました.
これは型に関する注釈(型アノテーション)をつけることができる仕様です.
参考 : https://docs.python.org/ja/3/library/typing.html
"""

def add_numbers(a, b):
    return a + b

# MEMO : 怒られる
# print(add_numbers([1, 2, 3], 'hoge'))


def add_numbers_v2(a: int, b: int) -> int:
    return a + b

# MEMO : ヒントが出現
# add_numbers_v2(a: int, b: int) -> int
# b: int
# print(add_numbers_v2(3, 4))


# ワーク1 : 引数と戻り値に対して明示的に型をつけて安全な関数を完成させよう
def circle_area(r):
    pi = 3.14
    return r ** 2 * pi
