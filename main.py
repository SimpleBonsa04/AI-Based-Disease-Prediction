# import necessary libraries
import pandas as pd
import pickle
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# load and prepare dataset
def load_data(filepath):
    data = pd.read_csv(filepath)
    data = data.fillna("None")
    X = data.drop("Disease", axis=1)
    y = data["Disease"]
    X = pd.get_dummies(X)
    return X, y

# train machine learning model
def train_model(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    model = RandomForestClassifier(n_estimators=200,random_state=42)
    model.fit(X_train, y_train)
    # save trained model
    with open("disease_model.pkl", "wb") as f:
        pickle.dump(model, f)
    return model

# build symptom lookup dictionary
def build_symptom_lookup(symptom_columns):
    symptoms = sorted(set(col.split("_")[-1] for col in symptom_columns))
    symptom_map = {symptom: i for i, symptom in enumerate(symptom_columns)}
    return symptoms, symptom_map

# convert user symptoms to model input vector
def create_input_vector(user_symptoms, symptom_columns):
    input_vector = np.zeros(len(symptom_columns))
    for i, column in enumerate(symptom_columns):
        for symptom in user_symptoms:
            if symptom in column:
                input_vector[i] = 1
    return pd.DataFrame([input_vector], columns=symptom_columns)


# main program
def main():
    # load data & train model
    X, y = load_data("disease_and_symptoms_training.csv")
    model = train_model(X, y)
    
    # extract symptoms
    symptom_columns = X.columns
    available_symptoms = sorted(set(col.split("_")[-1] for col in symptom_columns))
    while True:
        print("\nWhat symptoms are you experiencing?")
        print("Example symptoms:", ", ".join(available_symptoms[:10]))
        print("Type 'stop' to stop")
        user_input = input("Symptoms: ").lower()
        if user_input == "stop":
            print("Exiting system...Get Well Soon")
            break
        user_symptoms = [sym.strip() for sym in user_input.split(",")]

        # convert symptoms to vector, predict disease, probability of prediction
        input_vector = create_input_vector(user_symptoms, symptom_columns)
        prediction = model.predict(input_vector)[0]
        confidence = max(model.predict_proba(input_vector)[0])
        print("\nPredicted Disease:", prediction)
        print("Confidence:", round(confidence * 100, 2), "%")

# run program
if __name__ == "__main__":
    main()