import numpy as np
from flask import Flask, request, jsonify, render_template
import tensorflow as tf
import pickle
from tensorflow.keras.preprocessing.sequence import pad_sequences

app = Flask(__name__)

## Load the model
# model = pickle.load(open('model.pkl', 'rb'))
# model = tf.keras.models.load_model('hotel_review_model.h5')
model = tf.keras.models.load_model('hotel_review_model.h5', custom_objects={
    'Adam': lambda **kwargs: hvd.DistributedOptimizer(keras.optimizers.Adam(**kwargs))
})
# with open('model.pkl', 'rb') as f:
#     model = pickle.load(f)

## Load the tokenizer
with open('tokenizer.pkl', 'rb') as f:
    tokenizer = pickle.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():

    int_features =  [request.form['review']]

    final_features = request.form['review']

    sample_sequences = tokenizer.texts_to_sequences(int_features)
    fakes_padded = pad_sequences(sample_sequences, padding='post', maxlen=50) 
    
    output = model.predict(fakes_padded)
    print(type(output))
    if output>0.6:
        sentiment_pred = 'Positive review'
    elif output<0.4:
        sentiment_pred = 'Negative review'
    else:
        sentiment_pred = 'Neutral review'


    for x in range(len(int_features)):
        print(int_features[x])
        print(output[x])
        print('\n')

    return render_template('index.html', prediction_text='Predicted Sentiment {}'.format(output), text=final_features, sentiment=sentiment_pred)

@app.route('/results',methods=['POST'])
def results():

    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)