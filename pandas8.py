#車の燃費データを列'mpg'の昇順に並べ替えてみよう．そのためには，データフレームのsort_valuesメソッドを用いる．
#これだと燃費の悪い順に並ぶので，良い順に並べてみよう．そのためには，引数の ascending を False に設定すればよい（既定値はTrueで昇順）．
import pandas as pd
L = [
    "mpg",
    "cylinders",
    "displacement",
    "horsepower",
    "weight",
    "acceleration",
    "year",
    "origin",
    "name",
]
car = pd.read_csv(
    "http://logopt.com/data/auto-mpg.data", delim_whitespace=True, names=L
)
car.sort_values("mpg", ascending=False).head()
