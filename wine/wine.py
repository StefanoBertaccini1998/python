import pandas as pd

file_path = "../beginner_datasets/wine.csv"

df = pd.read_csv(file_path)
# Visualizziamone le dimensioni, un'anteprima, e osserviamo i nomi di colonna;
print(df.shape)
print(df.sample())
print(df.columns)

# Qual è la media di concentrazione alcolica per ogni qualità? Ci sono differenze? E rispetto alla media totale?
print(df.groupby("quality")["alcohol"].mean())
print(df["alcohol"].mean())

# C'è differenza nella concentrazione alcolica per vini bianchi e vini rossi?
print(df.groupby("type")["alcohol"].mean())

# Rifacendo le analisi delle domande precedenti ma per il pH, cambia qualcosa?
print(df.groupby("quality")["pH"].mean())
print(df.groupby("type")["pH"].mean())

# E per i solfati?
print(df.groupby("quality")["sulphates"].mean())
print(df.groupby("type")["sulphates"].mean())

