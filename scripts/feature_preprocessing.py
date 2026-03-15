def get_available_symptoms(symptom_columns):
  symptoms = sorted(set(col.split("_")[-1] for col in symptom_columns))
  return symptoms