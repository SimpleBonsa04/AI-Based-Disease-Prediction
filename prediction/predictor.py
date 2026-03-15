def predict_disease(model, input_vector):
    prediction = model.predict(input_vector)[0]
    confidence = max(model.predict_proba(input_vector)[0])
    return prediction, confidence