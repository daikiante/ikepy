"""
■標準ライブラリ : argparse
"""

# MEMO : argparseをインポート
import argparse

# MEMO : パーサーを作成
parser = argparse.ArgumentParser(description='このプログラムの説明(なくてもよい)')

# MEMO : parser.add_argumentで受け取る引数を追加していく
parser.add_argument('--input', '-i', type=str, help='この引数の説明(なくてもよい)')

# MEMO : 引数の解析準備
args = parser.parse_args()

# MEMO : parser.parse_args().引数名 として呼び出す
input_args = args.input
print(input_args)


# ワーク1 : 2つの引数を受け取って以下の文章を完成させてみよう
print(f'私の名前は{args.name}です。趣味は{args.desc}です。')