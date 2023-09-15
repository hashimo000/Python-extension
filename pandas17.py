#データには多くのNaN（欠損値）を含まれる．欠損値のある行を削除するには dropnaメソッド を用いる．
import pandas as pd
ufo = pd.read_csv("http://logopt.com/data/ufo.csv", index_col=0)
ufo.dropna().tail()
