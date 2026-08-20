
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

#############################################################################
# import numpy as np

# from sklearn.linear_model import LogisticRegression
# from sklearn.metrics import log_loss, accuracy_score

# # -----------------------------
# # TRAINING DATA
# # -----------------------------

# X = np.array([[1], [2], [3], [4], [5], [6]])

# y = np.array([0, 0, 0, 1, 1, 1])


# # -----------------------------
# # CREATE MODEL
# # -----------------------------

# model = LogisticRegression()


# # -----------------------------
# # TRAIN MODEL
# # -----------------------------

# model.fit(X, y)


# # -----------------------------
# # GET COEFFICIENT AND INTERCEPT
# # -----------------------------

# b1 = model.coef_[0][0]
# b0 = model.intercept_[0]

# print("Coefficient:", b1)
# print("Intercept:", b0)


# # -----------------------------
# # CALCULATE z
# # -----------------------------

# z = b0 + b1 * X.flatten()

# print("\nz values:")
# print(z)


# # -----------------------------
# # SIGMOID
# # -----------------------------

# probability = 1 / (1 + np.exp(-z))

# print("\nProbabilities:")
# print(probability)


# # -----------------------------
# # PREDICTION
# # -----------------------------

# prediction = (probability >= 0.5).astype(int)

# print("\nPredictions:")
# print(prediction)


# # -----------------------------
# # LOG LOSS
# # -----------------------------

# loss = log_loss(y, probability)

# print("\nLog Loss:", loss)


# # -----------------------------
# # ACCURACY
# # -----------------------------

# accuracy = accuracy_score(y, prediction)

# print("Accuracy:", accuracy)


# import numpy as np
# from sklearn.linear_model import LogisticRegression
# from sklearn.metrics import (
#     accuracy_score,
#     precision_score,
#     recall_score,
#     f1_score,
#     confusion_matrix,
#     log_loss
# )

# # Hours studied
# X = np.array([
#     [1],
#     [2],
#     [3],
#     [4],
#     [5],
#     [6],
#     [7],
#     [8],
#     [9],
#     [10]
# ])

# # Actual result
# # 0 = Fail
# # 1 = Pass
# y = np.array([
#     0,
#     0,
#     1,   # unusual: passed with only 3 hours
#     0,   # unusual: failed with 4 hours
#     1,
#     1,
#     0,   # unusual: failed with 7 hours
#     1,
#     1,
#     1
# ])

# # Create model
# model = LogisticRegression()

# # Train
# model.fit(X, y)

# # Probability of Pass
# probability = model.predict_proba(X)[:, 1]

# # Final prediction
# y_pred = model.predict(X)

# print("Probability:")
# print(probability)

# print("\nActual:")
# print(y)

# print("\nPredicted:")
# print(y_pred)

# # Accuracy
# accuracy = accuracy_score(y, y_pred)

# # Precision
# precision = precision_score(y, y_pred)

# # Recall
# recall = recall_score(y, y_pred)

# # F1
# f1 = f1_score(y, y_pred)

# # Confusion Matrix
# cm = confusion_matrix(y, y_pred)

# # Log Loss
# loss = log_loss(y, probability)

# print("\nAccuracy:", accuracy)
# print("Precision:", precision)
# print("Recall:", recall)
# print("F1 Score:", f1)

# print("\nConfusion Matrix:")
# print(cm)

# print("\nLog Loss:", loss)

# import numpy as np

# from sklearn.linear_model import LogisticRegression

# from sklearn.metrics import (
#     accuracy_score,
#     precision_score,
#     recall_score,
#     f1_score,
#     confusion_matrix,
#     log_loss
# )


# # ==========================================
# # 1. DATA
# # ==========================================

# # Hours studied
# X = np.array([
#     [1],
#     [2],
#     [3],
#     [4],
#     [5],
#     [6],
#     [7],
#     [8],
#     [9],
#     [10]
# ])

# # Actual result
# # 0 = Fail
# # 1 = Pass

# y = np.array([
#     0,
#     0,
#     0,
#     1,
#     1,
#     1,
#     0,   # unusual
#     1,
#     1,
#     1
# ])


# # ==========================================
# # 2. CREATE LOGISTIC REGRESSION MODEL
# # ==========================================

# model = LogisticRegression()


# # ==========================================
# # 3. TRAIN THE MODEL
# # ==========================================

# model.fit(X, y)


# # ==========================================
# # 4. GET COEFFICIENT AND INTERCEPT
# # ==========================================

# b1 = model.coef_[0][0]
# b0 = model.intercept_[0]

# print("Coefficient:", b1)
# print("Intercept:", b0)


# # ==========================================
# # 5. CALCULATE z
# # ==========================================

# z = b0 + b1 * X.flatten()

# print("\nz values:")
# print(z)


# # ==========================================
# # 6. SIGMOID
# # ==========================================

# probability = 1 / (1 + np.exp(-z))

# print("\nProbability of Pass:")
# print(probability)


# # ==========================================
# # 7. THRESHOLD
# # ==========================================

# threshold = 0.5

# y_pred = (probability >= threshold).astype(int)

# print("\nActual:")
# print(y)

# print("\nPredicted:")
# print(y_pred)


# # ==========================================
# # 8. CONFUSION MATRIX
# # ==========================================

# cm = confusion_matrix(y, y_pred)

# print("\nConfusion Matrix:")
# print(cm)


# # ==========================================
# # 9. ACCURACY
# # ==========================================

# accuracy = accuracy_score(y, y_pred)

# print("\nAccuracy:", accuracy)


# # ==========================================
# # 10. PRECISION
# # ==========================================

# precision = precision_score(y, y_pred)

# print("Precision:", precision)


# # ==========================================
# # 11. RECALL
# # ==========================================

# recall = recall_score(y, y_pred)

# print("Recall:", recall)


# # ==========================================
# # 12. F1 SCORE
# # ==========================================

# f1 = f1_score(y, y_pred)

# print("F1 Score:", f1)


# # ==========================================
# # 13. LOG LOSS
# # ==========================================

# loss = log_loss(y, probability)

# print("Log Loss:", loss)
##############################################################
# import numpy as np

# # ==========================================
# # 1. DATA
# # ==========================================

# # Hours studied
# X = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], dtype=float)

# # Actual result
# # 0 = Fail
# # 1 = Pass

# y = np.array([
#     0, 0, 0, 1, 1,
#     1, 0, 1, 1, 1
# ], dtype=float)


# # ==========================================
# # 2. INITIAL VALUES
# # ==========================================

# # Starting coefficient
# b1 = 0.0

# # Starting intercept
# b0 = 0.0

# # Learning rate
# learning_rate = 0.1

# # Number of times we train/update
# epochs = 10000


# # ==========================================
# # 3. SIGMOID FUNCTION
# # ==========================================

# def sigmoid(z):

#     return 1 / (1 + np.exp(-z))


# # ==========================================
# # 4. LOG LOSS FUNCTION
# # ==========================================

# def log_loss(y, p):

#     # Prevent log(0)
#     p = np.clip(p, 1e-15, 1 - 1e-15)

#     loss = -np.mean(
#         y * np.log(p) +
#         (1 - y) * np.log(1 - p)
#     )

#     return loss


# # ==========================================
# # 5. GRADIENT DESCENT
# # ==========================================

# for epoch in range(epochs):

#     # --------------------------------------
#     # STEP 1: Calculate z
#     # --------------------------------------

#     z = b0 + b1 * X


#     # --------------------------------------
#     # STEP 2: Convert z to probability
#     # --------------------------------------

#     p = sigmoid(z)


#     # --------------------------------------
#     # STEP 3: Calculate Log Loss
#     # --------------------------------------

#     loss = log_loss(y, p)


#     # --------------------------------------
#     # STEP 4: Calculate gradients
#     # --------------------------------------

#     db0 = np.mean(p - y)

#     db1 = np.mean((p - y) * X)


#     # --------------------------------------
#     # STEP 5: Update intercept
#     # --------------------------------------

#     b0 = b0 - learning_rate * db0


#     # --------------------------------------
#     # STEP 6: Update coefficient
#     # --------------------------------------

#     b1 = b1 - learning_rate * db1


#     # --------------------------------------
#     # Print progress
#     # --------------------------------------

#     if epoch % 1000 == 0:

#         print(
#             "Epoch:", epoch,
#             "Loss:", loss,
#             "b0:", b0,
#             "b1:", b1
#         )


# # ==========================================
# # 6. FINAL MODEL
# # ==========================================

# print("\nFINAL MODEL")

# print("Intercept (b0):", b0)

# print("Coefficient (b1):", b1)


# # ==========================================
# # 7. FINAL z
# # ==========================================

# z = b0 + b1 * X


# # ==========================================
# # 8. FINAL PROBABILITY
# # ==========================================

# p = sigmoid(z)

# print("\nProbabilities:")

# print(p)


# # ==========================================
# # 9. FINAL PREDICTION
# # ==========================================

# threshold = 0.5

# y_pred = (p >= threshold).astype(int)

# print("\nActual:")

# print(y.astype(int))

# print("\nPredicted:")

# print(y_pred)


# # ==========================================
# # 10. CONFUSION MATRIX MANUALLY
# # ==========================================

# TP = np.sum((y == 1) & (y_pred == 1))

# TN = np.sum((y == 0) & (y_pred == 0))

# FP = np.sum((y == 0) & (y_pred == 1))

# FN = np.sum((y == 1) & (y_pred == 0))


# print("\nConfusion Matrix Values")

# print("TP:", TP)

# print("TN:", TN)

# print("FP:", FP)

# print("FN:", FN)


# # ==========================================
# # 11. ACCURACY
# # ==========================================

# accuracy = (TP + TN) / (TP + TN + FP + FN)


# # ==========================================
# # 12. PRECISION
# # ==========================================

# precision = TP / (TP + FP)


# # ==========================================
# # 13. RECALL
# # ==========================================

# recall = TP / (TP + FN)


# # ==========================================
# # 14. F1 SCORE
# # ==========================================

# f1 = 2 * (precision * recall) / (precision + recall)


# # ==========================================
# # 15. FINAL LOG LOSS
# # ==========================================

# final_loss = log_loss(y, p)


# print("\nFINAL METRICS")

# print("Accuracy:", accuracy)

# print("Precision:", precision)

# print("Recall:", recall)

# print("F1 Score:", f1)

# print("Log Loss:", final_loss)

###############################################
# import numpy as np

# from sklearn.linear_model import LogisticRegression

# from sklearn.metrics import (
#     accuracy_score,
#     precision_score,
#     recall_score,
#     f1_score,
#     confusion_matrix,
#     log_loss
# )


# # ==========================================
# # 1. DATA
# # ==========================================

# # Hours studied
# X = np.array([
#     [1],
#     [2],
#     [3],
#     [4],
#     [5],
#     [6],
#     [7],
#     [8],
#     [9],
#     [10]
# ])

# # Actual result
# # 0 = Fail
# # 1 = Pass

# y = np.array([
#     0,
#     0,
#     0,
#     1,
#     1,
#     1,
#     0,   # unusual
#     1,
#     1,
#     1
# ])


# # ==========================================
# # 2. CREATE LOGISTIC REGRESSION MODEL
# # ==========================================

# model = LogisticRegression()


# # ==========================================
# # 3. TRAIN THE MODEL
# # ==========================================

# model.fit(X, y)


# # ==========================================
# # 4. GET COEFFICIENT AND INTERCEPT
# # ==========================================

# b1 = model.coef_[0][0]
# b0 = model.intercept_[0]

# print("Coefficient:", b1)
# print("Intercept:", b0)


# # ==========================================
# # 5. CALCULATE z
# # ==========================================

# z = b0 + b1 * X.flatten()

# print("\nz values:")
# print(z)


# # ==========================================
# # 6. SIGMOID
# # ==========================================

# probability = 1 / (1 + np.exp(-z))

# print("\nProbability of Pass:")
# print(probability)


# # ==========================================
# # 7. THRESHOLD
# # ==========================================

# threshold = 0.6

# y_pred = (probability >= threshold).astype(int)

# print("\nActual:")
# print(y)

# print("\nPredicted:")
# print(y_pred)


# # ==========================================
# # 8. CONFUSION MATRIX
# # ==========================================

# cm = confusion_matrix(y, y_pred)

# print("\nConfusion Matrix:")
# print(cm)


# # ==========================================
# # 9. ACCURACY
# # ==========================================

# accuracy = accuracy_score(y, y_pred)

# print("\nAccuracy:", accuracy)


# # ==========================================
# # 10. PRECISION
# # ==========================================

# precision = precision_score(y, y_pred)

# print("Precision:", precision)


# # ==========================================
# # 11. RECALL
# # ==========================================

# recall = recall_score(y, y_pred)

# print("Recall:", recall)


# # ==========================================
# # 12. F1 SCORE
# # ==========================================

# f1 = f1_score(y, y_pred)

# print("F1 Score:", f1)


# # ==========================================
# # 13. LOG LOSS
# # ==========================================

# loss = log_loss(y, probability)

# print("Log Loss:", loss)

# #####################################################
# import numpy as np

# from sklearn.preprocessing import PolynomialFeatures
# from sklearn.linear_model import LinearRegression
# from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


# # -----------------------------
# # DATA
# # -----------------------------

# X = np.array([
#     [1],
#     [2],
#     [3],
#     [4],
#     [5]
# ])

# y = np.array([
#     13,
#     18,
#     25,
#     34,
#     45
# ])


# # -----------------------------
# # CREATE POLYNOMIAL FEATURES
# # -----------------------------

# poly = PolynomialFeatures(degree=2)

# X_poly = poly.fit_transform(X)

# print("Original X:")
# print(X)

# print("\nPolynomial X:")
# print(X_poly)


# # -----------------------------
# # CREATE LINEAR REGRESSION
# # -----------------------------

# model = LinearRegression()


# # -----------------------------
# # TRAIN
# # -----------------------------

# model.fit(X_poly, y)


# # -----------------------------
# # GET COEFFICIENTS
# # -----------------------------

# print("\nIntercept:", model.intercept_)

# print("Coefficients:", model.coef_)


# # -----------------------------
# # PREDICTION#
# # -----------------------------

# y_pred = model.predict(X_poly)

# print("\nActual:")
# print(y)

# print("\nPredicted:")
# print(y_pred)


# # -----------------------------
# # ERROR
# # -----------------------------

# mae = mean_absolute_error(y, y_pred)

# mse = mean_squared_error(y, y_pred)

# rmse = np.sqrt(mse)

# r2 = r2_score(y, y_pred)


# print("\nMAE:", mae)

# print("MSE:", mse)

# print("RMSE:", rmse)

# print("R2:", r2)

#########################################################################
# import numpy as np

# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LogisticRegression

# from sklearn.metrics import (
#     accuracy_score,
#     precision_score,
#     recall_score,
#     f1_score,
#     confusion_matrix,
#     log_loss
# )


# # ==========================================
# # 1. DATA
# # ==========================================

# # Age and Salary
# X = np.array([
#     [22, 25000],
#     [25, 30000],
#     [28, 35000],
#     [30, 40000],
#     [32, 45000],
#     [35, 50000],
#     [38, 55000],
#     [40, 60000],
#     [42, 65000],
#     [45, 70000],
#     [23, 28000],
#     [27, 32000],
#     [31, 42000],
#     [36, 48000],
#     [41, 58000]
# ])

# # 0 = Did not buy
# # 1 = Bought
# y = np.array([
#     0,
#     0,
#     0,
#     1,
#     1,
#     1,
#     1,
#     1,
#     1,
#     1,
#     0,
#     0,
#     1,
#     1,
#     1
# ])


# # ==========================================
# # 2. SPLIT DATA
# # ==========================================

# X_train, X_test, y_train, y_test = train_test_split(
#     X,
#     y,
#     test_size=0.2,
#     random_state=42,
#     stratify=y
# )


# # ==========================================
# # 3. CREATE MODEL
# # ==========================================

# model = LogisticRegression()


# # ==========================================
# # 4. TRAIN
# # ==========================================

# model.fit(X_train, y_train)


# # ==========================================
# # 5. COEFFICIENTS
# # ==========================================

# print("Intercept:")
# print(model.intercept_)

# print("\nCoefficients:")
# print(model.coef_)


# # ==========================================
# # 6. PREDICTION
# # ==========================================

# y_pred = model.predict(X_test)


# # ==========================================
# # 7. PROBABILITY
# # ==========================================

# y_probability = model.predict_proba(X_test)[:, 1]


# print("\nActual:")
# print(y_test)

# print("\nPredicted:")
# print(y_pred)

# print("\nProbability of buying:")
# print(y_probability)


# # ==========================================
# # 8. CONFUSION MATRIX
# # ==========================================

# cm = confusion_matrix(y_test, y_pred)

# print("\nConfusion Matrix:")
# print(cm)


# # ==========================================
# # 9. ACCURACY
# # ==========================================

# accuracy = accuracy_score(y_test, y_pred)

# print("\nAccuracy:", accuracy)


# # ==========================================
# # 10. PRECISION
# # ==========================================

# precision = precision_score(
#     y_test,
#     y_pred,
#     zero_division=0
# )

# print("Precision:", precision)


# # ==========================================
# # 11. RECALL
# # ==========================================

# recall = recall_score(
#     y_test,
#     y_pred,
#     zero_division=0
# )

# print("Recall:", recall)


# # ==========================================
# # 12. F1 SCORE
# # ==========================================

# f1 = f1_score(
#     y_test,
#     y_pred,
#     zero_division=0
# )

# print("F1 Score:", f1)


# # ==========================================
# # 13. LOG LOSS
# # ==========================================

# loss = log_loss(
#     y_test,
#     y_probability
# )

# print("Log Loss:", loss)

################################################
# import numpy as np

# from sklearn.preprocessing import PolynomialFeatures
# from sklearn.linear_model import LinearRegression

# from sklearn.metrics import (
#     mean_absolute_error,
#     mean_squared_error,
#     r2_score
# )


# # ==========================================
# # 1. DATA
# # ==========================================

# # Hours studied
# X = np.array([
#     [1],
#     [2],
#     [3],
#     [4],
#     [5]
# ])

# # Actual exam scores
# y = np.array([
#     13,
#     18,
#     25,
#     34,
#     45
# ])


# # ==========================================
# # 2. CREATE POLYNOMIAL FEATURES
# # ==========================================

# # Degree 2 means:
# # X → X and X²

# poly = PolynomialFeatures(degree=2)

# X_poly = poly.fit_transform(X)


# print("Original X:")
# print(X)

# print("\nPolynomial X:")
# print(X_poly)


# # ==========================================
# # 3. CREATE LINEAR REGRESSION MODEL
# # ==========================================

# model = LinearRegression()


# # ==========================================
# # 4. TRAIN THE MODEL
# # ==========================================

# model.fit(X_poly, y)


# # ==========================================
# # 5. SHOW LEARNED PARAMETERS
# # ==========================================

# print("\nIntercept (b0):")
# print(model.intercept_)

# print("\nCoefficients:")
# print(model.coef_)


# # ==========================================
# # 6. PREDICT
# # ==========================================

# y_pred = model.predict(X_poly)


# print("\nActual values:")
# print(y)

# print("\nPredicted values:")
# print(y_pred)


# # ==========================================
# # 7. MAE
# # ==========================================

# mae = mean_absolute_error(y, y_pred)

# print("\nMAE:")
# print(mae)


# # ==========================================
# # 8. MSE
# # ==========================================

# mse = mean_squared_error(y, y_pred)

# print("\nMSE:")
# print(mse)


# # ==========================================
# # 9. RMSE
# # ==========================================

# rmse = np.sqrt(mse)

# print("\nRMSE:")
# print(rmse)


# # ==========================================
# # 10. R²
# # ==========================================

# r2 = r2_score(y, y_pred)

# print("\nR²:")
# print(r2)


# # ==========================================
# # 11. PREDICT A NEW VALUE
# # ==========================================

# new_X = np.array([[6]])

# # IMPORTANT:
# # New data must go through the same
# # polynomial transformation.

# new_X_poly = poly.transform(new_X)

# new_prediction = model.predict(new_X_poly)


# print("\nNew input:")
# print(new_X)

# print("\nNew polynomial features:")
# print(new_X_poly)

# print("\nPrediction for 6 hours:")
# print(new_prediction)

######################################################################
# import numpy as np

# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LinearRegression

# from sklearn.metrics import (
#     mean_absolute_error,
#     mean_squared_error,
#     r2_score
# )


# # ==========================================
# # 1. DATA
# # ==========================================

# # Features:
# # X1 = House size (sq ft)
# # X2 = Number of bedrooms
# # X3 = House age (years)

# X = np.array([
#     [1000, 2, 10],
#     [1200, 2, 8],
#     [1500, 3, 6],
#     [1800, 3, 5],
#     [2000, 4, 4],
#     [2200, 4, 3],
#     [2500, 4, 2],
#     [2800, 5, 2],
#     [3000, 5, 1],
#     [3500, 5, 1]
# ])


# # Target:
# # House price in lakhs

# y = np.array([
#     50,
#     58,
#     70,
#     82,
#     92,
#     102,
#     115,
#     130,
#     140,
#     160
# ])


# # ==========================================
# # 2. SPLIT DATA
# # ==========================================

# X_train, X_test, y_train, y_test = train_test_split(
#     X,
#     y,
#     test_size=0.2,
#     random_state=42
# )


# # ==========================================
# # 3. CREATE MODEL
# # ==========================================

# model = LinearRegression()


# # ==========================================
# # 4. TRAIN MODEL
# # ==========================================

# model.fit(X_train, y_train)


# # ==========================================
# # 5. GET INTERCEPT
# # ==========================================

# print("Intercept (b0):")
# print(model.intercept_)


# # ==========================================
# # 6. GET COEFFICIENTS
# # ==========================================

# print("\nCoefficients:")
# print(model.coef_)


# # ==========================================
# # 7. PREDICT TEST DATA
# # ==========================================

# y_pred = model.predict(X_test)


# print("\nActual prices:")
# print(y_test)

# print("\nPredicted prices:")
# print(y_pred)


# # ==========================================
# # 8. MAE
# # ==========================================

# mae = mean_absolute_error(y_test, y_pred)

# print("\nMAE:")
# print(mae)


# # ==========================================
# # 9. MSE
# # ==========================================

# mse = mean_squared_error(y_test, y_pred)

# print("\nMSE:")
# print(mse)


# # ==========================================
# # 10. RMSE
# # ==========================================

# rmse = np.sqrt(mse)

# print("\nRMSE:")
# print(rmse)


# # ==========================================
# # 11. R²
# # ==========================================

# r2 = r2_score(y_test, y_pred)

# print("\nR²:")
# print(r2)


# # ==========================================
# # 12. PREDICT A NEW HOUSE
# # ==========================================

# # New house:
# # Size = 2300 sq ft
# # Bedrooms = 4
# # Age = 3 years

# new_house = np.array([
#     [3500, 5, 1]
# ])


# new_prediction = model.predict(new_house)


# print("\nNew house:")
# print(new_house)

# print("\nPredicted price:")
# print(new_prediction)






# import kagglehub

# # Download latest version
# path = kagglehub.dataset_download("yasserh/housing-prices-dataset")

# print("Path to dataset files:", path)