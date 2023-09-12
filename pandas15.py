import pandas as pd
drinks = pd.read_csv("http://logopt.com/data/drinks.csv")
drinks.drop("continent", axis=1).head()
drinks.drop(2, axis=0).head()  # インデックス２の行を削除
