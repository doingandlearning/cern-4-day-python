import pandas as pd
import matplotlib.pyplot as plt
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

gym_data = pd.read_csv("./gym_membership.csv", index_col="id")
print(gym_data) # the head and the tail
print(gym_data.dtypes) # sense check the data types
print(gym_data.describe())
print(gym_data.shape)


print(gym_data['gender'])

filtered_df = gym_data[gym_data['Age'] > 40]
print(filtered_df[filtered_df['gender'] == "Male"])

sorted_by_age = gym_data.sort_values(by="Age")
print(sorted_by_age["Age"])

group_abonoment_type = gym_data.groupby('abonoment_type')
print(group_abonoment_type['Age'].mean())

plt.figure(figsize=(4,4))
group_abonoment_type['Age'].plot.hist(alpha=0.4)
plt.show()
