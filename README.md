# MLOps Linear Regression Pipeline

This project builds an end-to-end MLOps pipeline for a simple Linear Regression model using the California Housing dataset. It includes training, testing, quantization, Dockerization, and CI/CD using GitHub Actions.

## 📁 Folder Structure
```
├── src/
│ ├── train.py # Model training and saving
│ ├── quantize.py # Manual quantization of model weights
│ ├── predict.py # Inference using quantized weights
│ ├── utils.py # Shared helper functions
│ └── init.py
│
├── tests/
│ └── test_train.py # Unit tests for model training
│
├── .github/
│ └── workflows/
│ └── ci.yml # GitHub Actions CI/CD pipeline
│
├── Dockerfile
├── requirements.txt
├── README.md
└── .gitignore
```

## Pipeline Steps

1. Model Training
2. Testing
3. Manual Quantization
4. Dockerization
5. GitHub Actions CI/CD

## Commands used:

1. Set Up Virtual Environment
    - python -m venv venv
    - .\venv\Scripts\Activate.ps1 
    - pip install -r requirements.txt
      
2. Running the Pipeline Locally
    - Train Model 
        .  python -m src.train
    - Run Unit Tests
        . pytest
    - Quantization
        . python -m src.quantize
    - Run Inference from Quantized Model
        . python src/predict.py
      
3. Docker Usage
    - docker build -t my-predict-app .
    - docker run --rm my-predict-app
      
4. Ci/CI Pipeline Github Actions
    The GitHub Actions workflow (ci.yml) performs the following on every push to main:
        - ✅ test-suite
        - ✅ train-and-quantize
        - ✅ docker-check

## Comparison Table

| Step               | Method Used        | Output Artifact        |
|--------------------|--------------------|------------------------|
| Model Training     | scikit-learn (Linear Regression)      | `model.joblib`         |
| Unit Testing       | pytest             | Test report              |
| Manual Quantization       | NumPy Manual       | `quant_params.joblib`  |
| Dequant Inference    | NumPy dot + intercept | `unquant_params.joblib` |
| Dockerization      | Docker             | Docker container runs `predict.py`        |
| CI/CD              | GitHub Actions     | `.github/workflows/ci.yml`          |

🧑‍💻 **Author
Name: Manisha Bhalla
Roll No: G24AI1073
Email: G24AI1073@iitj.ac.in**
