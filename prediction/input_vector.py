import numpy as np
import pandas as pd
def create_input_vector(user_symptoms, symptom_columns):
  input_vector = np.zeros(len(symptom_columns))
  for i, column in enumerate(symptom_columns):
   for symptom in user_symptoms:
    if symptom in column:
      input_vector[i] = 1
  return pd.DataFrame([input_vector], columns=symptom_columns)