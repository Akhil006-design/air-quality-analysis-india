
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Step 1: Load the dataset
df = pd.read_csv("data/city_day.csv")

# Step 2: Select PM2.5 and AQI columns
df = df[["PM2.5", "AQI"]].dropna()

# Step 3: Prepare input (X) and output (y)
X = df[["PM2.5"]]
y = df["AQI"]

# Step 4: Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Step 5: Create and train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Step 6: Predict AQI for the test data
y_pred = model.predict(X_test)

# Step 7: Evaluate the model
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("AIR QUALITY LINEAR REGRESSION")
print("--------------------------------")
print("Total usable records:", len(df))
print("Training records:", len(X_train))
print("Testing records:", len(X_test))
print("Mean Absolute Error (MAE):", round(mae, 2))
print("Mean Squared Error (MSE):", round(mse, 2))
print("R-squared (R2):", round(r2, 3))
print("Model coefficient:", round(model.coef_[0], 3))
print("Model intercept:", round(model.intercept_, 3))
