# employee_Project
This is my employee salary prediction project 


# 🧑‍💼 Employee Salary Prediction Project

This is a **Machine Learning + Flask web application** that predicts an employee’s salary based on multiple factors such as age, gender, department, job title, years of experience, and education level.  

The project demonstrates the full cycle of:
1. Data preprocessing and model training  
2. Model deployment using Flask  
3. Interactive web pages for salary prediction and history tracking  

---

## 🚀 Features
- 📊 **Salary Prediction** based on input fields:
  - Age
  - Gender
  - Department
  - Job Title
  - Experience (years)
  - Education level
- 🖥️ **Web Pages**:
  - **Home** – Main landing page  
  - **About** – Info about project  
  - **Project** – Salary prediction form  
  - **History** – View previous predictions
- 🔮 Uses a trained **Random Forest model** (`Employee_model`)  
- 📝 Keeps a history of predictions during a session  

---

## 🛠️ Tech Stack
- **Python 3**  
- **Flask** – Web framework  
- **Pandas, NumPy** – Data preprocessing  
- **Scikit-learn, Joblib** – Model training & saving  
- **HTML, CSS** – Frontend  

---

## 📂 Project Structure
employee_Project/
│── app.py # Flask application
│── Employee_model # Trained ML model (joblib file)
│── basic.ipynb # Notebook: basic data exploration
│── employee.ipynb # Notebook: model training
│── templates/ # HTML pages
│ ├── index.html # Home page
│ ├── about.html # About project
│ ├── project.html # Salary prediction form
│ └── history.html # Prediction history
│── static/ # (Optional: CSS files)
│── README.md # Documentation


Copy
Edit

---

## ⚙️ Installation & Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/priyanshu37357/employee_Project.git
   cd employee_Project
Install required libraries:

bash
Copy
Edit
pip install flask pandas numpy scikit-learn joblib
Run the Flask app:

bash
Copy
Edit
python app.py
Open in browser:
 http://127.0.0.1:5000
cpp
Copy
Edit
http://127.0.0.1:5000/
📸 Sample Output (Console)

Copy
Edit
output>>>>> 24 1 0 3 4 1
Prediction for model: 33258.45
Browser shows:
Predicted Salary: ₹ 33258.45

🤝 Contributing
Pull requests are welcome. For significant changes, please open an issue first to discuss.

📝 License
This project is licensed under the MIT License.


Copy
Edit

