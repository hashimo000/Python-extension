import pandas as pd 
#車の燃費データを加速(acceleration)の良い順（大きいほど良い）に並べてみよう．どの車が一番加速が良いか？
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
car.sort_values("acceleration", ascending=False).head()