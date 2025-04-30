this is code 

import pandas as pd
import scipy.stats as stats

df = pd.read_csv("cleaned_udemy_data.csv")

BF = df[df['subject'] == 'Business Finance']['price']
GD = df[df['subject'] == 'Graphic Design']['price']
t_test, p_value = stats.ttest_ind(BF,GD,equal_var=False)

print(t_test,p_value)
