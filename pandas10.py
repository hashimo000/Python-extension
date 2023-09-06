import pandas as pd
L = [
    "mpg",
    "cylinders",
    "displacement",
    "horsepower",
    "weight",
    "acceleration",
    "year",
    "origin",
    "name",
]
car = pd.read_csv(
    "http://logopt.com/data/auto-mpg.data", delim_whitespace=True, names=L
)
car.sort_values("weight", ascending=False).head()