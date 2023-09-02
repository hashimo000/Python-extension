import pandas as pd
#iloc属性を用いて5番目から8番目までの行の2,3列目を抽出せよ．
jp = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data", index_col=0)
jp.iloc[4:7,1:2]