import pandas as pd

s = pd.Series([1,2,3,4,5,6, 7])

print(s.count())
print(s.mean())
print(s.quantile([0.25, 0.5, 0.75]))
print(s.describe())

df = pd.DataFrame()
df["Name"] = pd.Series(["Albane", "Salvatore", "Sevgi", "Matthias"])
df["COI"] = pd.Series(["France", "Italy", "Turkey", "Austria"])
print(df)
print(df.describe())





