#以下の国別のアルコール摂取量のデータを用いて，大陸(continent)別のビール，蒸留酒，ワインの摂取量の平均を求めよ
import pandas as pd

# データの読み込み
drinks = pd.read_csv("http://logopt.com/data/drinks.csv")

# 大陸(continent)ごとのビール(beer_servings)、蒸留酒(spirit_servings)、ワイン(wine_servings)の摂取量の平均を計算
continent_avg = drinks.groupby('continent').mean()[['beer_servings', 'spirit_servings', 'wine_servings']]

print(continent_avg)
