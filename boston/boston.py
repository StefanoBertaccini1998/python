import pandas as pd

file_path = "../beginner_datasets/boston.csv"

df = pd.read_csv(file_path)
# Visualizziamone le dimensioni, un'anteprima, e osserviamo i nomi di colonna;
print(df.shape)
print(df.sample())
print(df.columns)

# La media del prezzo delle case cambia a seconda della distanza dal fiume Charles?
print(df.groupby("chas")["medv"].mean() * 1000)

# Si nota una correlazione tra il tasso di criminalità e il valore delle abitazioni?
correlation = df.loc[:,["crim", "medv"]]
print(correlation.corr())
