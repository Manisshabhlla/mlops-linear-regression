# MLOps Linear Regression Pipeline

This project builds an end-to-end MLOps pipeline for a simple Linear Regression model using the California Housing dataset.

## Pipeline Steps

1. Model Training
2. Testing
3. Manual Quantization
4. Dockerization
5. GitHub Actions CI/CD

## Comparison Table

| Step               | Method Used        | Output Artifact        |
|--------------------|--------------------|------------------------|
| Model Training     | scikit-learn       | `model.joblib`         |
| Unit Testing       | pytest             | Test logs              |
| Quantization       | NumPy Manual       | `quant_params.joblib`  |
| Dockerization      | Docker             | Container Image        |
| CI/CD              | GitHub Actions     | Auto Pipeline          |
