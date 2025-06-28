# 🧠 ML Web Application

A machine learning web application built with Flask that loads a pre-trained model and serves predictions through a simple user interface. Includes Docker support and is deployable to platforms like Heroku.

---

## 🚀 Features

- Flask-powered web application
- Pre-trained ML model for inference
- Docker support for containerized deployment
- GitHub Actions for CI/CD
- Ready for deployment on Heroku

---

## 🛠️ Getting Started

### 🔧 Prerequisites

- Python 3.8+
- `pip` package manager
- Docker (optional, for containerization)

### 📦 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Srijanprasad/ML.git
   cd ML
Create a virtual environment and activate it:

bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Windows use venv\Scripts\activate
Install dependencies:

bash
Copy
Edit
pip install -r requirement.txt
🖥️ Running the Application
🔧 Locally
bash
Copy
Edit
python app.py
Then open http://127.0.0.1:5000 in your browser.

🐳 Using Docker
bash
Copy
Edit
docker build -t ml-web-app .
docker run -p 5000:5000 ml-web-app
📊 Model Information
The trained model (model.pkl) is used for predictions via the web interface. Model training and evaluation are shown in first.ipynb.

🚀 Deployment
The application can be deployed on platforms like Heroku using the procfile and Docker support. GitHub Actions in .github/ can be used for automated deployment pipelines.

📄 License
This project is licensed under the terms of the MIT License. See the LICENSE file for details.

🙌 Acknowledgments
Developed and maintained by Srijan Prasad. Contributions are welcome!


---


