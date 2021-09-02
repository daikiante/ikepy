# 現場で使えるイケてるPython2021
## 概要
いけぱいをダウンロードいただきありがとうございます。\
本講座では"Pythonの文法は覚えたけど実際現場ではどうやって使っているの？"という悩みのもとPython初心者から中級者を目指していきます。

## 講座を受講して実現できること

* 脱初心者
```Python
# bad exsample
if n == 10:
    x = 'OK'
else :
    x = 'NG'

# good exsample
x = 'OK' if n == 10 else 'NG'
```
* 組み込み関数やメソッドの活用方法がわかる
```Python
# bad exsample
print('ゼロまでの距離は' + abs(number) + 'です')

# good exsample
print(f'ゼロまでの距離は{abs(number)}です')
```
* 処理の高速化を意識したコードが書ける

```Python
# bad exsample
text_list = []
for file in Path('hoge').glob('*.txt'):
    text_list.append(file.name)

# good exsample
text_list = [file.name for file in Path('hoge').glob('*.txt')]
```

## バージョン

* Python 3.6.9
* Anaconda 4.10.3

※Python3.5以上であれば大丈夫です。

## 環境構築

初学者にはanacondaを推奨しています。\
標準ライブラリの学習に焦点を当てているので必要なライブラリはありません。

## 最後に
素敵なPythonライフを！