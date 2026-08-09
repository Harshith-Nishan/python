
import numpy as np

# Step 1: Dataset
X = np.array([
    [2.5, 2.4],
    [0.5, 0.7],
    [2.2, 2.9],
    [1.9, 2.2],
    [3.1, 3.0],
    [2.3, 2.7],
    [2.0, 1.6],
    [1.0, 1.1],
    [1.5, 1.6],
    [1.1, 0.9]
])

# Step 2: Calculate Mean
mean = np.mean(X, axis=0)

# Step 3: Center the Data
X_centered = X - mean

# Step 4: Covariance Matrix
cov_matrix = np.cov(X_centered.T)

# Step 5: Eigenvalues and Eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(cov_matrix)

# Step 6: Sort Eigenvalues
idx = np.argsort(eigenvalues)[::-1]
eigenvalues = eigenvalues[idx]
eigenvectors = eigenvectors[:, idx]

# Step 7: Select PC1
PC1 = eigenvectors[:, 0]

# Step 8: Project Data onto PC1
reduced_data = X_centered @ PC1

print("Mean:")
print(mean)

print("\nCentered Data:")
print(X_centered)

print("\nCovariance Matrix:")
print(cov_matrix)

print("\nEigenvalues:")
print(eigenvalues)

print("\nEigenvectors:")
print(eigenvectors)

print("\nPC1:")
print(PC1)

print("\nReduced Data:")
print(reduced_data)