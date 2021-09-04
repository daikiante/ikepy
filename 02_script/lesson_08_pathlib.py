"""
■標準ライブラリ : pathlib
"""

from pathlib import Path

text_dir = Path('../03_data')
# <class 'pathlib.PosixPath'>

texts = text_dir.glob('*.txt')
# <class 'generator'>

# MEMO : 中身を確認
for file in texts:
    # パスを取得
    print(file)
    
    # 拡張子つきファイル名を取得
    print(file.name)
    
    # ファイル名のみ取得
    print(file.stem)
    
    # 親ディレクトリを取得
    print(file.parent)
