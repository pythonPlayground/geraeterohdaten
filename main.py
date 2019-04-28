import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("test.csv", index_col=0)
print(data[["BG"], :])
print(data[:, ["Purger"]])
