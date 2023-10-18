from flask import Flask, render_template, request, jsonify
import joblib  # Import the library used to load your model

app = Flask(__name__)

# Load your trained model
model = joblib.load('model.pkl')  # Make sure 'model.pkl' is in the same directory

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get input data from the form
        tv = float(request.form['tv'])
        radio = float(request.form['radio'])
        newspaper = float(request.form['newspaper'])

        # Make a prediction using the model
        prediction = model.predict([[tv, radio, newspaper]])

        # Return the prediction as a JSON response
        return jsonify({'prediction': prediction[0]})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
