import numpy as np
import pandas as pd


years = 5 
a = pd.DataFrame({"Mese": list("GFMAMGLASOND"*years),
                  "Anno": np.repeat(list(range(years)), 12),
                  "Guadagni": np.random.randint(800, 5000, 12*years)})
print(a)
print(a.groupby('Anno')["Guadagni"].cumsum())
