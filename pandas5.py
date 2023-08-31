import pandas as pd
#インデックス列を指定するには、read_csvを用いてデータを読み込む際に、index_col引数で指定することができる。列の番号もしくは列名を与えることによって、指定した列がインデックスになる。
ufo = pd.read_csv("http://logopt.com/data/ufo.csv", index_col=0)  # column
ufo.head()