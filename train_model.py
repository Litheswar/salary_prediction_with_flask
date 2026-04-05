from sklearn.linear_model import LinearRegression
import numpy as np
import pickle
import os

X = np.array([[1], [2], [3], [4], [5]])
y = np.array([20000, 40000, 60000, 80000, 100000])

model = LinearRegression()
model.fit(X, y)


os.makedirs("models", exist_ok=True)

with open("models/model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model saved successfully!")
