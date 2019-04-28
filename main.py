import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("geraeterohdaten.csv", sep=";", index_col=0)
# print(data)
print(data.loc[["BGA"], :])
# print(data[:, ["Purger"]])
