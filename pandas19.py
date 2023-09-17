#上のUFOデータに対して，町(City列）の欠損値を"場所不明"に，色（Colors Reported列）の欠損値を"たぶん白"に置き換えよ．
import pandas as pd

# データの読み込み
ufo = pd.read_csv("http://logopt.com/data/ufo.csv", index_col=0)

# City列の欠損値を"場所不明"に置き換え
ufo['City'].fillna('場所不明', inplace=True)

# Colors Reported列の欠損値を"たぶん白"に置き換え
ufo['Colors Reported'].fillna('たぶん白', inplace=True)

# 結果の確認
print(ufo.head())
