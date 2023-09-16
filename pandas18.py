#欠損値を適当な値で置き換えたい場合にはfillnaメソッドを用いる．たとえば，欠損値NaNを "Unknown" で置き換えたい場合には，以下のようにする．
import pandas as pd
ufo = pd.read_csv("http://logopt.com/data/ufo.csv", index_col=0)
ufo.fillna("Unknown").tail()