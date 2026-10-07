# Heart Disease Prediction — End-to-End Machine Learning System

An end-to-end **Machine Learning project for heart disease prediction**, developed as part of **Machine Learning Fundamentals (AIC354), Assignment 2** at **COMSATS University Islamabad, Lahore Campus**.

The project follows a complete machine learning workflow, starting from data loading and preprocessing and ending with a deployed Streamlit web application.

> **Educational project only:** This system is developed for academic and learning purposes. It is **not a medical diagnostic tool** and should not be used for making real-world medical decisions.

---

## Project Information

| Detail                     | Information                                 |
| -------------------------- | ------------------------------------------- |
| **Course**                 | Machine Learning Fundamentals (AIC354)      |
| **Assignment**             | Assignment 2                                |
| **University**             | COMSATS University Islamabad, Lahore Campus |
| **Student**                | Hunain                                      |
| **Registration No.**       | FA24-BSE-083                                |
| **Instructor**             | Dr. Rao Muhammad Adeel Nawab                |
| **Machine Learning Model** | Support Vector Classifier (SVC)             |
| **Dataset**                | UCI Heart Disease — Cleveland Dataset       |
| **Application**            | Streamlit                                   |
| **Test Accuracy**          | **80%**                                     |

---

## Project Overview

The objective of this project is to build a machine learning system that predicts whether a patient is likely to have heart disease based on selected attributes from the **UCI Heart Disease (Cleveland)** dataset.

The implementation follows the workflow specified for the assignment:

```text
Import Libraries
       ↓
Load Data
       ↓
Data Preprocessing
       ↓
Label Encoding
       ↓
Train/Test Split
       ↓
Model Training
       ↓
Model Testing
       ↓
Application Development
       ↓
User Feedback
       ↓
Deployment
```

The trained model is integrated into a **Streamlit web application**, allowing users to enter the required patient attributes and receive a prediction.

---

## Features Used for Prediction

This project uses **4 selected input attributes** from the original dataset.

| User Input            | Dataset Column | Description             | Application Values    |
| --------------------- | -------------- | ----------------------- | --------------------- |
| **Gender**            | `sex`          | Patient's sex           | Male, Female          |
| **Exercise Angina**   | `exang`        | Exercise-induced angina | No, Yes               |
| **ST Depression**     | `oldpeak`      | ST depression value     | Absent, Mild, High    |
| **Number of Vessels** | `ca`           | Number of major vessels | Zero, One, Two, Three |

These attributes are processed and encoded before being provided to the trained machine learning model.

---

## Dataset

The project uses the **Heart Disease — Cleveland** dataset from the **UCI Machine Learning Repository** (https://archive.ics.uci.edu/dataset/45/heart+disease).

The original dataset contains multiple clinical attributes related to cardiovascular health. For this assignment, a subset of four features was selected for the prediction system.

The project directory contains the dataset and the processed/encoded versions used during the machine learning workflow.

### Dataset Processing

The data processing workflow includes:

1. Loading the dataset using Pandas (UCI `processed.cleveland.data`; 303 patients, 6 rows with missing values removed = 297).
2. Inspecting the available columns and data.
3. Selecting the required input features.
4. Converting the values into text categories (Male/Female, Yes/No, Absent/Mild/High, Zero-Three) removing the 6 rows with missing values, and converting the target so that `Yes` = heart disease present (`num` 1-4).
5. Encoding categorical features into numerical representations.
6. Preparing the target variable.
7. Splitting the data into training and testing sets.
8. Training the machine learning model.

---

## Machine Learning Model

### Support Vector Classifier (SVC)

The project uses a **Support Vector Classifier (SVC)** for binary classification.

SVC attempts to find an optimal decision boundary that separates different classes in the feature space. It is suitable for classification problems where the objective is to determine which class a particular input belongs to.

In this project, the model predicts whether the provided patient information indicates:

```text
Heart Disease
      OR
No Heart Disease
```

The trained model is saved as:

```text
svc_trained_model.pkl
```

This saved model is then loaded by the Streamlit application so that predictions can be generated without retraining the model every time the application runs.

---

## Model Performance

The model was evaluated using a held-out test set containing **60 patients**.

### Test Results

| Metric        |          Score |
| ------------- | -------------: |
| **Accuracy**  | **0.80 (80%)** |
| **Precision** |       **0.80** |
| **Recall**    |       **0.80** |
| **F1-Score**  |       **0.80** |

### Accuracy

The model achieved approximately **80% accuracy** on the test dataset.

This means that the model correctly classified approximately 80% of the samples in the held-out test set.

> The reported performance is based on the selected features, preprocessing steps, dataset split, and model configuration used in this academic project.

---

## Project Structure

```text
Heart-Disease-Prediction/
│
├── 2 - Heart Disease Prediction/
│   ├── Heart_Disease_Prediction.ipynb
│   ├── Heart_Disease_Prediction.html
│   ├── heart-disease-original-cleveland.csv
│   ├── sample-data.csv
│   ├── sample-data-encoded-output.csv
│   ├── sample-data-encoded.csv
│   ├── training-data-encoded.csv
│   ├── testing-data-encoded.csv
│   ├── model-predictions.csv
│   ├── svc_trained_model.pkl
│   └── requirements.txt
│
├── streamlit-app/
│   ├── app.py
│   ├── svc_trained_model.pkl
│   ├── sample-data.csv
│   ├── requirements.txt
│   ├── runtime.txt
│   ├── .streamlit/config.toml
│   └── README.md
│
├── .streamlit/config.toml
├── Assignment_2_Documentation.docx
├── DEPLOY_STEPS.md
├── requirements.txt
├── runtime.txt
└── README.md
```

## Streamlit Web Application

The trained model is integrated into a **Streamlit** application.

The application provides a simple interface where users can select the required input values:

* Gender
* Exercise Angina
* ST Depression
* Number of Vessels

After submitting the information, the application processes the inputs using the same encoding approach used during model training and passes them to the saved SVC model.

The resulting prediction is then displayed to the user.

### Live Demo

**[Heart Disease Prediction — Streamlit App](https://heart-disease-hunain-uci.streamlit.app/)**


---

## Running the Project Locally

### 1. Clone the Repository

```bash
git clone https://github.com/Hunain-Riasat/HEART-DISEASE-PREDICTOR.git
cd HEART-DISEASE-PREDICTOR
```

### 2. Create a Virtual Environment

Windows:

```bash
python -m venv venv
```

Activate it:

```bash
venv\Scripts\activate
```

For macOS/Linux:

```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Jupyter Notebook

```bash
jupyter notebook
```

Open:

```text
2 - Heart Disease Prediction/Heart_Disease_Prediction.ipynb
```

The notebook contains the complete machine learning implementation.

---

## Running the Streamlit Application

Navigate to the application directory:

```bash
cd streamlit-app
```

Install the application dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

The application will open in the browser through the local Streamlit server.

---

## Technologies Used

### Programming Language

* **Python**

### Machine Learning

* **Scikit-learn**
* Support Vector Classifier (SVC)

### Data Processing

* **Pandas**
* **NumPy**
* **Matplotlib** and **Seaborn** (charts)

### Model Persistence

* **Pickle**

### Development Environment

* **Jupyter Notebook**
* **Jupyter HTML Export**

### Web Application

* **Streamlit**

### Deployment

* **Streamlit Community Cloud**

---

## Key Learning Outcomes

Through this project, the following machine learning concepts were implemented:

* Loading and exploring a real-world dataset
* Data preprocessing
* Feature selection
* Label encoding
* Training and testing datasets
* Classification using SVC
* Model evaluation
* Accuracy, precision, recall, and F1-score
* Saving a trained machine learning model
* Integrating an ML model into a web application
* Deploying a machine learning application to the cloud

---


## Disclaimer

This project is intended **strictly for educational and academic purposes** as part of the Machine Learning Fundamentals course.

The predictions generated by this application **must not be considered medical advice or a professional diagnosis**. Anyone with concerns about heart disease or other health conditions should consult a qualified healthcare professional.

---

## Author

**Muhammad Hunain Riasat**

BS Software Engineering
COMSATS University Islamabad, Lahore Campus

**Registration No.:** FA24-BSE-083

---

## License

This project is intended for educational purposes. Please refer to the repository for any applicable licensing information.

