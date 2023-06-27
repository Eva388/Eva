import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import math as mt
from lmfit import models

df = pd.read_csv('triton.csv')

print(df.head())