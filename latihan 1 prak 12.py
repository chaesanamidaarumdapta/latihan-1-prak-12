import pandas as pd
print("Data Science")

Data = pd.read_csv("negara.csv")

f = pd.DataFrame(Data)
mean = f.groupby(["Benua"]).mean()
std = f.groupby(["Benua"]).std()

print(f)
print(mean)
print(std)
