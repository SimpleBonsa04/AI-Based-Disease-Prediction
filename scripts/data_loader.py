import pandas as pd
def load_data(filepath):
    data = pd.read_csv(filepath)
    data = data.fillna("None")
    X = data.drop("Disease", axis=1)
    y = data["Disease"]
    X = pd.get_dummies(X)
    return X, y