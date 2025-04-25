import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("udemy_courses.csv")
df = df.dropna()
df['published_timestamp'] = pd.to_datetime(df['published_timestamp'])

df['subject'] = df['subject'].str.strip()
df['level'] = df['level'].str.strip()
df.columns = df.columns.str.lower().str.replace(' ', '_')

df.to_csv("cleaned_udemy_data.csv", index=False)
