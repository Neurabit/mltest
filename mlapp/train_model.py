# predict/train_model.py

import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

# Sample Data (you can replace this with actual data or load from a CSV)
data = {
    'bedrooms': [1, 2, 3, 4, 5],
    'bathrooms': [1, 2, 2, 3, 3],
    'size': [600, 800, 1200, 1500, 2000],
    'price': [150000, 180000, 250000, 300000, 400000]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Features and target variable
X = df[['bedrooms', 'bathrooms', 'size']]  # Features
y = df['price']  # Target variable

# Train the model
model = LinearRegression()
model.fit(X, y)

# Save the model using joblib
joblib.dump(model, 'mlapp/house_price_model.pkl')

print("Model trained and saved!")
