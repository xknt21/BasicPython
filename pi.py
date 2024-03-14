text = """
    How I want a drink, alcoholic of course, after the heavy chapters involving
    quantum mechanics. All of thy geometry, Herr Planck, is fairly hard.
"""

# TODO

pi = list(map(len, text.replace(",","").replace(".","").split())) 
#replace...文字列を指定して置換。第一引数に置換元文字列、第二引数に置換先引数を指定。
#split...区切り文字で分割。デフォルトは空白文字で分割する。戻り値はリスト。

print("".join(map(str, pi)))
#join...リスト等のイテレータを引数として受け取り、それらを連結・結合する。
#mapオブジェクト...map関数の戻り値は、リストではなくmapオブジェクトというiterableなオブジェクト。list型に変更する必要はない。