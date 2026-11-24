import numpy as np

print("Name: Eric")
print("Surname: Tamele")
print("ID: 70274")

seed_ET = 274
np.random.seed(seed_ET)

sumID_ET = 20
A_ET = np.random.rand(sumID_ET, 4)

print(f"\nA shape: {A_ET.shape}")
print(f"A sum: {A_ET.sum()}")

d_ET = 5
D_ET = np.zeros((sumID_ET, sumID_ET))

for i in range(sumID_ET):
    for j in range(sumID_ET):
        if i != j:
            diff = np.abs(A_ET[i] - A_ET[j])
            dist_ET = np.sum(diff**d_ET) ** (1/4)
            D_ET[i, j] = dist_ET
        else:
            D_ET[i, i] = np.inf

nearest_ET = np.argmin(D_ET, axis=1)

print(f"\nD shape: {D_ET.shape}")
print(f"D sum: {D_ET[np.isfinite(D_ET)].sum()}")

print("\nPoints and their nearest neighbors:")
for i in range(sumID_ET):
    nearest_idx_ET = nearest_ET[i]
    distance_ET = D_ET[i, nearest_idx_ET]
    print(f"Point {i}: {A_ET[i]} -> Nearest: {A_ET[nearest_idx_ET]}, Distance: {distance_ET:.6f}")