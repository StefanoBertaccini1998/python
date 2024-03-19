import pandas as pd

file_path = "../dataset/Mappa-dei-pub-circoli-locali-in-Italia.json"

df = pd.read_json(file_path, encoding="latin1")

for column in df.columns:
    # Refine for your refactor
    cleanColumn = column[1:]
    df.rename(columns={f'{column}': f'{cleanColumn}'}, inplace=True)
print(df.columns)

# quanti dati ci sono in totale?
print(df.shape)

# quali sono i metadati?


# stampiamo il primo elemento
print(df.head(1))

# stampiamo l'ultimo elemento
print(df.tail(1))

# riusciamo a stampare un elemento a caso?
print(df.sample(1))

# quali sono gli anni di inserimento presenti?
print(df.get("anno_inserimento").unique())

# quante attività ci sono nel quadrato di longitudine 9-10 e latitudine 45-46?
lat_long = (((df["longitudine"] >= 9) & (df["longitudine"] <= 10)) & (
        (df["latitudine"] >= 45) & (df["latitudine"] <= 46)))

print(df[lat_long])

filtro_long_lat = (df.longitudine.between(9.0, 10.0)) & (df.latitudine.between(45.0, 46.0))
print(df[filtro_long_lat])

# quante attività ci sono nella provincia di Vicenza?

citta_vicenza = (df.provincia == "VICENZA")

print(df[citta_vicenza])

# quante enoteche ci sono, e come si chiamano?


# quante attività ci sono in Lazio e Abruzzo assieme?

lazio_abruzzo = (df.regione == "Lazio") | (df.regione == "Abruzzo")

print(df[lazio_abruzzo].count())
