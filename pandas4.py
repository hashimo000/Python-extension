import pandas as pd
L = ['mpg', 'cylinders', 'displacement', 'horsepower','weight', 'acceleration','year','origin', 'name']
url="http://logopt.com/data/auto-mpg.data"

car=pd.read_csv(url,delim_whitespace=True, names=L)
#データを確認してみると，このデータはカンマ(,)区切り（これがread_csv関数の既定値）ではなく，空白で区切られている．

#このような場合には，read_csvの引数の delim_whitespace をTrueに設定しておく必要がある．
print(car.head())
car.tail()