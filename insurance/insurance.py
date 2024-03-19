import pandas as pd

file_path = "../beginner_datasets/insurance.csv"

df = pd.read_csv(file_path)
# Visualizziamone le dimensioni, un'anteprima, e osserviamo i nomi di colonna;
print(df.shape)
print(df.sample())
print(df.columns)

# Quali sono le medie di charges rispetto a region? Ci sono differenze significative?
print(df.groupby("region")["charges"].mean())
print(df.groupby("smoker")["charges"].mean())
print(df.groupby("sex")["charges"].mean())

# Quali sono i descrittori statistici di bmi? Quali sono minimo, media e massimo di charges rispetto ai diversi
# quartili dei valori di bmi?
statistic = df["bmi"].describe()
print(statistic)

print(df.groupby("bmi")["charges"].describe().transpose())
