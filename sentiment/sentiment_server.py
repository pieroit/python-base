from flask import Flask, request, jsonify
from joblib import load

# carico modello e vettorizzatore
vectorizer = load('sentiment_vectorizer.joblib')
model = load('sentiment_model.joblib')

# dichiara servizio
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def sentiment():
    text = request.json['text']
    print(text)

    # QUI PULIZIA

    vectorized_texts = vectorizer.transform( [text] )
    prediction = model.predict(vectorized_texts)
    prediction_proba = model.predict_proba(vectorized_texts)

    prediction_proba = dict(zip(model.classes_, prediction_proba[0]))

    reply = {
        'prediction': prediction[0],
        'probability': prediction_proba
    }

    return jsonify(reply)

app.run()
