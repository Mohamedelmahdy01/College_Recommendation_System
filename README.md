
# College Recommendation System

This project is a machine-learning-powered web application that predicts the most suitable college for a user based on their preferences, learning styles, and career goals. It consists of a Flask-based API and a user-friendly web interface.

---

## Features
- Interactive form for collecting user preferences and skills.
- Backend prediction API that returns the recommended college.
- Handles both categorical and numerical inputs.

---

## Project Structure

```
├── app.py                    # Flask API code
├── college_recommendation_model.pkl  # Trained ML model
├── college_label_encoders.pkl        # Label encoders for input data
├── college_target_encoder.pkl        # Encoder for target predictions
├── college_recommendation_dataset.csv  
├── README.md                 
```

---

## Setup Instructions

### 1. Install Required Libraries
Ensure Python is installed. Install the necessary Python libraries using:
```bash
pip install flask pandas joblib
```

### 2. Start the Flask API
Run the `app.py` file to start the backend server:
```bash
python app.py
```
The API will be available at `http://127.0.0.1:5000`.

### 3. Access the API
Test the API using Postman, cURL, or any client by sending a POST request to the `/predict` endpoint.

---

## API Details

### Endpoint
**URL:** `http://127.0.0.1:5000/predict`  
**Method:** `POST`  
**Content-Type:** `application/json`

### Input JSON Structure

The API accepts the following fields in the JSON payload:

1. **Categorical Fields** (Choose one option for each):
   - `Hands-on Projects`: **Yes** or **No**
   - `Work Style`: **Both**, **Independent**, or **Teamwork**
   - `Career Goal`: **Researcher**, **Engineer**, **Manager**, or **Artist**
   - `Hobbies`: **Music**, **Painting**, **Sports**, or **Writing**
   - `Competitions`: **Yes** or **No**
   - `Learning Preference`: **Practical**, **Theory**, or **Both**
   - `Study Abroad`: **Yes** or **No**
   - `Study Close to Home`: **Yes** or **No**

2. **Numeric Fields** (Rated from 1 to 5):
   - Academic skills: **Math**, **Physics**, **Chemistry**, **Biology**, **Literature**, **History**, **Computer Science**
   - Personal and interpersonal skills: **Problem Solving**, **Public Speaking**, **Group Discussions**
   - Financial factor: **Tuition Importance**

### Example Input
```json
{
  "Math": 2,
  "Physics": 1,
  "Chemistry": 5,
  "Biology": 2,
  "Literature": 4,
  "History": 2,
  "Computer Science": 5,
  "Problem Solving": 5,
  "Hands-on Projects": "No",
  "Public Speaking": 3,
  "Work Style": "Independent",
  "Career Goal": "Engineer",
  "Hobbies": "Programming",
  "Competitions": "Yes",
  "Learning Preference": "Practical",
  "Group Discussions": 3,
  "Study Abroad": "Yes",
  "Tuition Importance": 1,
  "Study Close to Home": "No"
}
```

### Example Response
```json
{
    "predicted_college": "Business School"
}
```

---

## Usage Notes
- **Input Validation:** Ensure all required fields are included in the request.
- **Numeric Fields:** Values must be integers between 1 and 5.
- **Categorical Fields:** Must match predefined options (case-sensitive).

---

## Testing the API

You can test the API using **Postman** or cURL:

### Using Postman:
1. Open Postman and create a new `POST` request.
2. Set the URL to `http://127.0.0.1:5000/predict`.
3. Add a JSON body with the required fields.
4. Send the request and view the predicted college.

### Using cURL:
```bash
curl -X POST http://127.0.0.1:5000/predict -H "Content-Type: application/json" -d '{
    "Math": 2,
    "Physics": 1,
    "Chemistry": 5,
    "Biology": 2,
    "Literature": 4,
    "History": 2,
    "Computer Science": 5,
    "Problem Solving": 5,
    "Hands-on Projects": "No",
    "Public Speaking": 3,
    "Work Style": "Independent",
    "Career Goal": "Engineer",
    "Hobbies": "Programming",
    "Competitions": "Yes",
    "Learning Preference": "Practical",
    "Group Discussions": 3,
    "Study Abroad": "Yes",
    "Tuition Importance": 1,
    "Study Close to Home": "No"
}'
```

---

## Future Improvements
- Add authentication for secure access.
- Deploy the API and frontend to a cloud platform like AWS, Heroku, or PythonAnywhere.
- Enhance the user interface with modern frameworks like React or Vue.js.

---

Feel free to contribute to this project or suggest improvements! 🚀
