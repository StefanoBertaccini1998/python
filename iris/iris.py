import pandas as pd

file_path = "../beginner_datasets/iris.csv"

df = pd.read_csv(file_path)
# Visualizziamone le dimensioni, un'anteprima, e osserviamo i nomi di colonna;
print(df.shape)
print(df.sample())
print(df.columns)

# La media della lunghezza dei petali di tutto il dataset
print(df["petal_length"].mean().round(2))

# La media della lunghezza dei petali per ogni specie di Iris, utilizzando il metodo .groupby()
print(df.groupby("species")["petal_length"].mean())

# Media, minimo e massimo della larghezza dei sepali per ogni specie, utilizzando .groupby() e .agg()
print(df.groupby("species")["sepal_width"].agg("mean", "min", "max"))
