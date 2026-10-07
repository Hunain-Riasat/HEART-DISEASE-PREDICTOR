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
| **Dataset**                | Kaggle Heart Disease — Cleveland Dataset    |
| **Application**            | Streamlit                                   |
| **Test Accuracy**          | **79%**                                     |

---

## Project Overview

The objective of this project is to build a machine learning system that predicts whether a patient is likely to have heart disease based on selected attributes from the **Kaggle Heart Disease (Cleveland)** dataset.

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

The project uses the **Heart Disease — Cleveland** dataset available through Kaggle.

The original dataset contains multiple clinical attributes related to cardiovascular health. For this assignment, a subset of four features was selected for the prediction system.

The project directory contains the dataset and the processed/encoded versions used during the machine learning workflow.

### Dataset Processing

The data processing workflow includes:

1. Loading the dataset using Pandas (Kaggle `heart.csv`, 303 patients).
2. Inspecting the available columns and data.
3. Selecting the required input features.
4. Converting the values into text categories (Male/Female, Yes/No, Absent/Mild/High, Zero-Three) and correcting the target so that `Yes` = heart disease present.
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

The model was evaluated using a held-out test set containing **61 patients**.

### Test Results

| Metric        |          Score |
| ------------- | -------------: |
| **Accuracy**  | **0.79 (79%)** |
| **Precision** |       **0.79** |
| **Recall**    |       **0.79** |
| **F1-Score**  |       **0.79** |

### Accuracy

The model achieved approximately **79% accuracy** on the test dataset.

This means that the model correctly classified approximately 79% of the samples in the held-out test set.

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

### Main Components

**`2 - Heart Disease Prediction/`**

Contains the complete machine learning notebook, dataset, processed data, predictions, and trained model.

**`Heart_Disease_Prediction.ipynb`**

Contains the complete ML workflow, including data loading, preprocessing, encoding, training, testing, evaluation, application and feedback phases, and deployment steps.

**`heart-disease-original-cleveland.csv`**

Original Cleveland dataset (303 patients) used for the project.

**`sample-data.csv`**

The 4 selected input attributes plus the output, converted into text labels (Male, Yes, Mild, Zero, ...).

**`sample-data-encoded.csv`, `training-data-encoded.csv`, `testing-data-encoded.csv`**

Label-encoded data, and its 80% training / 20% testing split.

**`model-predictions.csv`**

Predictions generated by the trained model on the testing data.

**`svc_trained_model.pkl`**

Serialized trained SVC model used by the deployed application.

**`streamlit-app/`**

Contains the web application used to interact with the trained model.

---

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

**[Heart Disease Prediction — Streamlit App](https://heart-disease-hunain.streamlit.app/)**

> Replace the URL above with the final Streamlit deployment URL if the application is redeployed under a different address.

---

## Running the Project Locally

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/your-repository-name.git
cd your-repository-name
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

## Machine Learning Workflow

### 1. Import Libraries

The required Python libraries are imported for:

* Data manipulation
* Data preprocessing
* Machine learning
* Model evaluation
* Saving/loading the trained model

Common libraries used include:

```text
Pandas
NumPy
Scikit-learn
Pickle
Matplotlib / Seaborn
PrettyTable
Streamlit
```

### 2. Load Data

The prepared dataset (4 selected attributes + output, built from the Cleveland `heart.csv`) is loaded using Pandas.

```python
import pandas as pd

sample_data = pd.read_csv("sample-data.csv")
```

### 3. Preprocess Data

The required columns are selected and prepared for machine learning.

Categorical values are converted into numerical representations so that they can be processed by the SVC model.

### 4. Label Encoding

The selected categorical features are encoded into numerical values.

For example:

```text
Male   → Numerical value
Female → Numerical value
```

Similarly, categorical values for exercise angina and the other selected features are converted into model-compatible values.

### 5. Train/Test Split

The processed data is divided into:

```text
Training Data (80% - 242 patients)
      +
Testing Data (20% - 61 patients)
```

The training data is used to learn the classification patterns, while the testing data is kept separate to evaluate model performance.

### 6. Model Training

An SVC model is trained using the processed training data.

```python
from sklearn.svm import SVC

model = SVC(gamma="auto", random_state=0)
model.fit(input_vector_train, output_label_train)
```

### 7. Model Testing

The trained model is evaluated using the unseen test data.

Performance metrics such as:

* Accuracy
* Precision
* Recall
* F1-score

are calculated to assess the classification performance.

### 8. Save the Trained Model

After training, the model is serialized and saved as:

```text
svc_trained_model.pkl
```

This allows the Streamlit application to load the already-trained model directly.

### 9. Application

The Streamlit interface collects the four required inputs from the user and passes the processed values to the trained model.

### 10. Feedback

The application displays the prediction result to the user, providing immediate feedback based on the entered values.

### 11. Deployment

The Streamlit application can be deployed to **Streamlit Community Cloud** so that it can be accessed through a web browser without running the application locally.

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

## Repository Contents

The repository includes both the **machine learning implementation** and the **deployed application**:

```text
Machine Learning Notebook
        ↓
Dataset
        ↓
Preprocessed Data
        ↓
Trained SVC Model
        ↓
Predictions
        ↓
Streamlit Application
        ↓
Cloud Deployment
```

This makes the project an end-to-end demonstration of taking a machine learning model from a dataset to a usable web application.

---

## Disclaimer

This project is intended **strictly for educational and academic purposes** as part of the Machine Learning Fundamentals course.

The predictions generated by this application **must not be considered medical advice or a professional diagnosis**. Anyone with concerns about heart disease or other health conditions should consult a qualified healthcare professional.

---

## Author

**Hunain Riasat**

BS Software Engineering
COMSATS University Islamabad, Lahore Campus

**Registration No.:** FA24-BSE-083

---

## License

This project is intended for educational purposes. Please refer to the repository for any applicable licensing information.

