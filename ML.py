import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score




df = pd.read_csv("cleaned_udemy_data.csv")
df = df.drop(columns=['course_id', 'course_title', 'url', 'published_timestamp'])
df = df.dropna()
df = pd.get_dummies(df, columns=['subject', 'level', 'is_paid'], drop_first=True)

x = df.drop("num_subscribers", axis=1)
y = df["num_subscribers"]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=11)
model = RandomForestRegressor(n_estimators=150, random_state=11 )

model.fit(x_train, y_train)

subscribers_pred = model.predict(x_test)

print("R² Score:", r2_score(y_test, subscribers_pred))
print("RMSE:", mean_absolute_error(y_test, subscribers_pred))
