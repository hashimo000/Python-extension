import pandas as pd

# irisデータセットを読み込む
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
column_names = ["sepal_length", "sepal_width", "petal_length", "petal_width", "class"]
df = pd.read_csv(url, names=column_names)

# loc属性を使用して'class'列を抽出
species_series = df.loc[:, 'class']

print(species_series)
