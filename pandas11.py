import pandas as pd
#データの抽出
df = pd.read_csv(
    "http://logopt.com/data/iris.data", names=["がく片長", "がく片幅", "花びら長", "花びら幅", "種類"]
)
df[df.がく片長 >= 7.0]
