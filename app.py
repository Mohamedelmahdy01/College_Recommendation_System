from flask import Flask, request, jsonify
import joblib
import pandas as pd

# Load the trained model and encoders
model = joblib.load('college_recommendation_model.pkl')
label_encoders = joblib.load('college_label_encoders.pkl')  # Correct file for label encoders
target_encoder = joblib.load('college_target_encoder.pkl')

# Create Flask app
app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Parse input JSON data
        input_data = request.get_json()
        if not input_data:
            return jsonify({'error': 'No input data provided.'}), 400

        # Convert input data to DataFrame
        input_df = pd.DataFrame([input_data])

        # Validate input columns
        expected_columns = list(label_encoders.keys())
        if not all(col in input_df.columns for col in expected_columns):
            return jsonify({'error': 'Invalid input data, some columns are missing.'}), 400

        # Encode categorical inputs
        for column, encoder in label_encoders.items():
            input_df[column] = encoder.transform(input_df[column].astype(str))  # Ensure input is string

        # Predict target using the model
        prediction = model.predict(input_df)
        predicted_college = target_encoder.inverse_transform(prediction)[0]

        # Return prediction as JSON
        return jsonify({'predicted_college': predicted_college})

    except KeyError as e:
        return jsonify({'error': f'Missing column in input: {str(e)}'}), 400
    except ValueError as e:
        return jsonify({'error': f'Value error: {str(e)}'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)  # Change to debug=False in production
