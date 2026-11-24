import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def mainET():
    nameET = "Eric"
    surnameET = "Tamele"
    idET = 70274
    print(nameET, surnameET, idET, sep=" | ")

    seedET = int(str(idET)[-3:])
    sumIDET = sum(int(dET) for dET in str(idET))
    print("seedET:", seedET)
    print("sumIDET:", sumIDET)

    dfET = pd.read_csv("exam1_data.csv")
    start_index_ET = sumIDET
    end_index_ET = start_index_ET + sumIDET

    subET = dfET.iloc[start_index_ET:end_index_ET]
    xET = subET["x"].to_numpy()
    yET = subET["y"].to_numpy()

    print("Info about x")
    print("len xET:", len(xET))
    print("sum xET:", xET.sum())
    print("first 3 xET:", xET[:3])
    print("last 3 xET:", xET[-3:])

    print("Info about y")
    print("len yET:", len(yET))
    print("sum yET:", yET.sum())
    print("first 3 yET:", yET[:3])
    print("last 3 yET:", yET[-3:])

    plt.figure(figsize=(8, 6))
    plt.scatter(xET, yET, color="blue", label="dataET")
    plt.xlabel("xET")
    plt.ylabel("yET")
    plt.title(f"{surnameET} {idET}")
    plt.legend()

    coeffsET = np.polyfit(xET, yET, deg=2)
    aET, bET, cET = coeffsET

    print("Model interceptET (cET):", cET)
    print("Model coefficientsET (aET, bET):", aET, bET)

    x_curve_ET = np.linspace(xET.min(), xET.max(), 200)
    y_curve_ET = aET * x_curve_ET**2 + bET * x_curve_ET + cET
    plt.plot(x_curve_ET, y_curve_ET, color="green", label="poly_deg2_ET")

    np.random.seed(seedET)

    x_new_ET = np.random.uniform(xET.min(), xET.max(), size=5)
    y_new_ET = aET * x_new_ET**2 + bET * x_new_ET + cET

    plt.scatter(x_new_ET, y_new_ET, color="red", label="new_points_ET")
    plt.legend()

    print("Sum of new xET:", x_new_ET.sum())

    print("Sum of new yET:", y_new_ET.sum())

    print("New (xET, yET) points:")
    for x_val_ET, y_val_ET in zip(x_new_ET, y_new_ET):
        print(x_val_ET, y_val_ET)

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    mainET()
