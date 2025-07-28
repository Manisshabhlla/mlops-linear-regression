# src/quantize.py
from joblib import load, dump
import numpy as np

model = load("model.joblib")

coeff = model.coef_
intercept = model.intercept_

dump((coeff, intercept), "unquant_params.joblib")

# Manual quantization (uint8 range assumption)
q_coeff = np.round((coeff - coeff.min()) / (coeff.max() - coeff.min()) * 255).astype(np.uint8)
q_intercept = np.round(intercept).astype(np.uint8)

dump((q_coeff, q_intercept), "quant_params.joblib")
