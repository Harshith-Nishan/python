
# import numpy as np

# # Step 1: Dataset
# X = np.array([
#     [2.5, 2.4],
#     [0.5, 0.7],
#     [2.2, 2.9],
#     [1.9, 2.2],
#     [3.1, 3.0],
#     [2.3, 2.7],
#     [2.0, 1.6],
#     [1.0, 1.1],
#     [1.5, 1.6],
#     [1.1, 0.9]
# ])

# # Step 2: Calculate Mean
# mean = np.mean(X, axis=0)

# # Step 3: Center the Data
# X_centered = X - mean

# # Step 4: Covariance Matrix
# cov_matrix = np.cov(X_centered.T)

# # Step 5: Eigenvalues and Eigenvectors
# eigenvalues, eigenvectors = np.linalg.eig(cov_matrix)

# # Step 6: Sort Eigenvalues
# idx = np.argsort(eigenvalues)[::-1]
# eigenvalues = eigenvalues[idx]
# eigenvectors = eigenvectors[:, idx]

# # Step 7: Select PC1
# PC1 = eigenvectors[:, 0]

# # Step 8: Project Data onto PC1
# reduced_data = X_centered @ PC1

# print("Mean:")
# print(mean)

# print("\nCentered Data:")
# print(X_centered)

# print("\nCovariance Matrix:")
# print(cov_matrix)

# print("\nEigenvalues:")
# print(eigenvalues)

# print("\nEigenvectors:")
# print(eigenvectors)

# print("\nPC1:")
# print(PC1)

# print("\nReduced Data:")
# print(reduced_data)

# import pandas as pd

# # -----------------------------------
# # ORIGINAL DATASET
# # -----------------------------------

# df = pd.DataFrame({
#     "Method": ["Video", "Book", "Classroom",
#                "Video", "Book", "Classroom"],
#     "Score": [80, 70, 75, 85, 65, 78]
# })

# print("ORIGINAL DATA:")
# print(df)


# # ===================================
# # 1. ONE-HOT ENCODING
# # ===================================

# one_hot = pd.get_dummies(
#     df["Method"],
#     dtype=int
# )

# print("\n\n1. ONE-HOT ENCODING:")
# print(one_hot)


# # ===================================
# # 2. DUMMY ENCODING
# # ===================================

# dummy = pd.get_dummies(
#     df["Method"],
#     drop_first=True,
#     dtype=int
# )

# print("\n\n2. DUMMY ENCODING:")
# print(dummy)


# # ===================================
# # 3. EFFECT ENCODING
# # ===================================

# effect = pd.DataFrame()

# effect["Video"] = df["Method"].map({
#     "Video": 1,
#     "Book": 0,
#     "Classroom": -1
# })

# effect["Book"] = df["Method"].map({
#     "Video": 0,
#     "Book": 1,
#     "Classroom": -1
# })

# print("\n\n3. EFFECT ENCODING:")
# print(effect)


# import numpy as np
# from sklearn.linear_model import LinearRegression

# # Training data
# # X = Hours studied
# # y = Score

# X = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)
# y = np.array([35, 42, 50, 58, 65])

# # Create the model
# model = LinearRegression()

# # Train the model
# model.fit(X, y)

# # Get slope and intercept
# print("Slope:", model.coef_[0])
# print("Intercept:", model.intercept_)

# # Predict score for a student who studied 6 hours
# prediction = model.predict([[2]])

# print("Predicted score:", prediction[0])

############################################################
# import numpy as np
# from sklearn.linear_model import LinearRegression
# from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# # X = input features
# # Column 1 = Hours studied
# # Column 2 = Sleep hours

# X = np.array([
#     [1, 6],
#     [2, 7],
#     [3, 7],
#     [4, 8],
#     [5, 8]
# ])

# # y = output
# y = np.array([35, 42, 50, 58, 65])

# # Create the model
# model = LinearRegression()

# # Train the model
# model.fit(X, y)

# # Get coefficients
# print("Coefficients:", model.coef_)
# print("Intercept:", model.intercept_)

# # Predict the training data
# y_pred = model.predict(X)

# print("\nActual:", y)
# print("Predicted:", y_pred)

# # Calculate errors
# mae = mean_absolute_error(y, y_pred)
# mse = mean_squared_error(y, y_pred)
# rmse = np.sqrt(mse)
# r2 = r2_score(y, y_pred)

# print("\nMAE:", mae)
# print("MSE:", mse)
# print("RMSE:", rmse)
# print("R2 Score:", r2)

# # Predict a new student
# # Hours = 6
# # Sleep = 7

# new_student = [[6, 7]]

# prediction = model.predict(new_student)

# print("\nPredicted score:", prediction[0])

###############################################################
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

X = np.array([
    [1, 6],
    [2, 6],
    [3, 7],
    [4, 7],
    [5, 8],
    [6, 8],
    [7, 9],
    [8, 9],
    [9, 10],
    [10, 10]
])

y = np.array([34, 42, 50, 58, 66, 74, 82, 90, 98, 106])

model = LinearRegression()

model.fit(X, y)

y_pred = model.predict(X)

print("Coefficients:", model.coef_)
print("Intercept:", model.intercept_)

print("MAE:", mean_absolute_error(y, y_pred))
print("MSE:", mean_squared_error(y, y_pred))
print("RMSE:", np.sqrt(mean_squared_error(y, y_pred)))
print("R2:", r2_score(y, y_pred))