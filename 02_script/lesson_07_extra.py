"""
■便利なビルドイン関数の紹介
"""

# print()   : ()内を表示する
print('hi')

# str()     : str型のオブジェクトを返す
number = 123
print(str(number))

# int()     : int型のオブジェクトを返す
string = '123'
print(int(string))

# float()   : float型のオブジェクトを返す
int_number = 5
print(float(int_number))

# bool()    : bool型のオブジェクトを返す。空、0、NoneはFalseを返す
print(bool(1))

# type()    : オブジェクトの型を返す
print(type(40))

# input()   : 文字列を入力する(入力値は文字列扱い)
input_str = input()
print(input_str)

# len()     : 要素数を取得する
print(len([5, 3, 2, 'hi', 5.666, True]))

# abs()     : 絶対値を返す
print(abs(-4))

# sum()     : 合計を返す
print(sum([90, 145]))

# max()     : 最大値を返す
print(max([1, 2, 3, 4, 5]))

# min()     : 最小値を返す
print(min([1, 2, 3, 4, 5]))

# pow(a, b) : aのb乗を返す
print(pow(5, 2))

# range()   : 指定範囲の整数列を返す
print([i for i in range(3)])

# round()   : 値を四捨五入する。第２引数は小数点以下の数
print(round(3.333333333333333333333333))
