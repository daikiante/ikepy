"""
■辞書内包表記
・基本(キーと値の2つを指定すること)
{キー: 値 for 任意の変数名 in イテラブルオブジェクト}

・条件式を追加することも可能(Trueとなる要素のみ追加される)
{キー: 値 for 任意の変数名 in イテラブルオブジェクト if 条件式}

※辞書には同じキーを2つ以上登録できないため、同じキーを指定した場合は上書きされる。
"""

# lenでキーを指定
name_list = ['SEVENELEVEn', 'FamilyMart', 'LAWSON']
name_dict = {name: len(name) for name in name_list}


# zipを使う
keys = [12, 13, 14]
values = ['Python', 'PHP', 'JavaScript']
sample_dict = {key: value for key, value in zip(keys, values)}


# enumerateを使う(iterにインデックスを付与)
kaizoku_list = ['Luffy', 'Nami', 'Zoro']
kaizoku_dict = {index: kaizoku for index, kaizoku in enumerate(kaizoku_list)}


# ワーク1 : インクリメントするインデックスをキーとして以下のリストを辞書にしてみよう
activitys = ['umi', 'kawa', 'yama']