"""
■無名関数 lambda
・ラムダ式
名前 = lambda 引数, 引数, ...: 式

・関数定義
def 名前(引数, 引数, ...):
    return 式

※PEP8ではlambda式には名前を付けないのが推奨されている
"""

# MEMO : まずは挙動を確認(今回は名前をつける)
multiple = lambda x: x*2
result = multiple(5)
# 10


# MEMO : mapと組み合わせる
numbers = [4, 5, 5, 7]
map_square = list(map(lambda x: x**2, numbers))
# [16, 25, 25, 49]


# MEMO : lambdaに複数の引数を渡す
add_a = 30
add_b = 49
add_function = lambda a, b: a + b
add_function(add_a, add_b)
# 79


# ワーク1 : mapとlambdaを組み合わせて要素に10%上乗せしたlistを作成しよう  ex)3000 -> 3300
prices = [3000, 2500, 10500, 4300]
