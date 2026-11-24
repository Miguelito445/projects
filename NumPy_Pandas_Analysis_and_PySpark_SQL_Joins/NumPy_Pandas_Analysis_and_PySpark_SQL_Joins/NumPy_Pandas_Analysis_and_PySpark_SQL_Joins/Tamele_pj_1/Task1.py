import numpy as np

print("Name: Eric")
print("Surname: Tamele")
print("ID: 70274")

seed = 274
id_0 = 274
id_1 = 7027
R = 14

np.random.seed(seed)

A_ET = np.random.randint(0, R, size=(id_0, id_1))

B_ET = np.random.randint(0, R, size=(id_0, id_1))

C_ET = np.random.randint(0, R, size=(id_0, id_1))

print(f"shape A = shape B = shape C = {A_ET.shape}")

print("\nInfo about A")
print(f"Sum of all numbers from A: {A_ET.sum()}")
print("First row of A:", A_ET[0])
print("Last row of A:", A_ET[-1])

print("\nInfo about B")
print(f"Sum of all numbers from B: {B_ET.sum()}")
print("First row of B:", B_ET[0])
print("Last row of B:", B_ET[-1])

print("\nInfo about C")
print(f"Sum of all numbers from C: {C_ET.sum()}")
print("First row of C:", C_ET[0])
print("Last row of C:", C_ET[-1])

A_wins_B_ET = np.sum(A_ET > B_ET)
A_loses_B_ET = np.sum(A_ET < B_ET)
A_ties_B_ET = np.sum(A_ET == B_ET)

print("\nA against B")
print(f"Sum of how many times A won against B: {A_wins_B_ET}")
print(f"Sum of how many times A lost to B: {A_loses_B_ET}")
print(f"Sum of how many times A tied with B: {A_ties_B_ET}")

A_wins_C_ET = np.sum(A_ET > C_ET)
A_loses_C_ET = np.sum(A_ET < C_ET)
A_ties_C_ET = np.sum(A_ET == C_ET)

print("\nA against C")
print(f"Sum of how many times A won against C: {A_wins_C_ET}")
print(f"Sum of how many times A lost to C: {A_loses_C_ET}")
print(f"Sum of how many times A tied with C: {A_ties_C_ET}")

B_wins_C_ET = np.sum(B_ET > C_ET)
B_loses_C_ET = np.sum(B_ET < C_ET)
B_ties_C_ET = np.sum(B_ET == C_ET)

print("\nB against C")
print(f"Sum of how many times B won against C: {B_wins_C_ET}")
print(f"Sum of how many times B lost to C: {B_loses_C_ET}")
print(f"Sum of how many times B tied with C: {B_ties_C_ET}")

print("\nA the winner")
A_total_wins_ET = A_wins_B_ET + A_wins_C_ET
print(f"Sum of how many times A won against B and C: {A_total_wins_ET}")

print("\nA the looser")
print(f"Sum of how many times A won against B and C: {A_total_wins_ET}")

print("\nB the winner")
B_total_wins_ET = (np.sum(B_ET > A_ET) + np.sum(B_ET > C_ET))
print(f"Sum of how many times B won against A and C: {B_total_wins_ET}")

print("\nB the looser")
B_total_losses_ET = (np.sum(B_ET < A_ET) + np.sum(B_ET < C_ET))
print(f"Sum of how many times B lost to A and C: {B_total_losses_ET}")

print("\nC the winner")
C_total_wins_ET = (np.sum(C_ET > A_ET) + np.sum(C_ET > B_ET))
print(f"Sum of how many times C won against A and B: {C_total_wins_ET}")

print("\nC the looser")
C_total_losses_ET = (np.sum(C_ET < A_ET) + np.sum(C_ET < B_ET))
print(f"Sum of how many times C lost to A and B: {C_total_losses_ET}")