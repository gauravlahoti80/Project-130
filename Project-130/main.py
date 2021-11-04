import pandas as pd

df = pd.read_csv('main.csv')

del df['planet_density']
del df['host_temperature']
del df['host_mass']
del df['host_radius']

df.to_csv('final.csv')
