import joblib



# Load your trained model (ensure you have a model file saved)
model = joblib.load('rf.pkl')

def get_ml_prediction(features):
    prediction = model.predict([features])
    return prediction[0]
