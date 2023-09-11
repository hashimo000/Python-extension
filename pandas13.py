#それを行う方法がグループ化であり，メソッド名はgroupbyだ．
import pandas as pd
df = pd.read_csv(
    "http://logopt.com/data/iris.data", names=["がく片長", "がく片幅", "花びら長", "花びら幅", "種類"]
)
df.groupby("種類").sum()