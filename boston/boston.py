import pandas as pd

file_path = "../beginner_datasets/boston.csv"

df = pd.read_csv(file_path)
# Visualizziamone le dimensioni, un'anteprima, e osserviamo i nomi di colonna;
print(df.shape)
print(df.sample())
print(df.columns)

