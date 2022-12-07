import numpy as np
import heartpy as hp
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('raw_ppg.csv')

df.keys()

plt.figure(figsize=(12,6))

plt.plot(df['ppg'].values)
plt.show()