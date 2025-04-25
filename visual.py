import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("cleaned_udemy_data.csv")

plt.figure(figsize=(10, 6))
sns.histplot(df['price'], bins=20, kde=True)
plt.title('Розподіл цін на курси на Udemy')
plt.xlabel('Ціна (USD)')
plt.ylabel('Кількість курсів')
plt.show()


corr = df[['price', 'num_reviews', 'content_duration']].corr()

plt.figure(figsize=(8, 6))
sns.heatmap(corr, annot=True, cmap="coolwarm", linewidths=0.5)
plt.title("Кореляційна матриця між ціною, кількістю відгуків і тривалістю курсу")
plt.show()


