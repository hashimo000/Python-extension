import pandas as pd

# 列名リスト
L = [ 'Alcohol', 'Malic','Ash', 'Alcalinity', 'Magnesium', 'Phenols', 'Flavanoids', 'Nonflavanoid', 'Proanthocyanins', 'Color', 'Hue', 'OD280', 'OD315', 'Proline']

# データを読み込む
url = "http://logopt.com/data/wine.data"
wine = pd.read_csv(url, header=None, names=L)

# 最後の5つのデータを表示する
print(wine.tail(5))