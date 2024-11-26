from flask import Flask, request, jsonify
import joblib
import pandas as pd

try:
    model = joblib.load('college_recommendation_model.pkl')
    label_encoders = joblib.load('college_label_encoders.pkl')
    target_encoder = joblib.load('college_target_encoder.pkl')
    print("Model and encoders loaded successfully.")
except Exception as e:
    print(f"Error loading model or encoders: {e}")
    exit(1)

app = Flask(__name__)
 
@app.route('/predict', methods=['POST'])
def predict():
    try:
        input_data = request.get_json()
        if not input_data:
            return jsonify({'error': 'No input data provided.'}), 400

        input_df = pd.DataFrame([input_data])

        expected_columns = list(label_encoders.keys())
        if not all(col in input_df.columns for col in expected_columns):
            return jsonify({'error': 'Invalid input data, some columns are missing.'}), 400

        for column, encoder in label_encoders.items():
            try:
                input_df[column] = encoder.transform(input_df[column].astype(str))
            except ValueError as e:
                return jsonify({'error': f"Invalid value for column {column}: {str(e)}. Valid values are: {list(encoder.classes_)}"}), 400

        prediction = model.predict(input_df)
        predicted_college = target_encoder.inverse_transform(prediction)[0]

        return jsonify({'predicted_college': predicted_college})

    except KeyError as e:
        return jsonify({'error': f'Missing column in input: {str(e)}'}), 400
    except ValueError as e:
        return jsonify({'error': f'Value error: {str(e)}'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)  
