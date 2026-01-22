#  Cyber Threat Detection System

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![PyTorch](https://img.shields.io/badge/PyTorch-2.0+-red.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Status-Production-success.svg)

**Deep Learning-powered cybersecurity threat detection using the BETH dataset**

[Demo](#-demo) • [Features](#-features) • [Installation](#-installation) • [Usage](#-usage) • [Architecture](#-architecture)

</div>

---

## 📋 Overview

A production-ready machine learning system that detects malicious cybersecurity events in real-time using neural networks. Built with PyTorch and deployed with a clean, modular architecture suitable for enterprise environments.

This project analyzes system event logs to classify threats with **99.5% validation accuracy**, helping security teams identify suspicious activities before they escalate into breaches.

### 🎯 Key Achievements

- ✅ **High Accuracy**: 99.5% validation accuracy on 188K+ events
- ✅ **Production-Ready**: Modular codebase with proper separation of concerns
- ✅ **Scalable Architecture**: Designed for integration with real-time monitoring systems
- ✅ **Reproducible**: Complete pipeline from data loading to inference

---

## 🚀 Features

- **Binary Classification**: Detects benign vs. malicious cybersecurity events
- **Deep Neural Network**: 3-layer architecture optimized for threat patterns
- **Standardized Preprocessing**: Feature scaling for robust predictions
- **Model Persistence**: Save/load trained models for deployment
- **Easy Integration**: Simple Python API for predictions
- **Comprehensive Logging**: Track training progress and model performance

---

## 🏗️ Architecture

### Model Design

```
Input Layer (7 features)
    ↓
Dense Layer (128 neurons) + ReLU
    ↓
Dense Layer (64 neurons) + ReLU
    ↓
Output Layer (1 neuron) + Sigmoid
    ↓
Binary Classification (0: Benign | 1: Threat)
```

### System Architecture

```
┌─────────────────┐
│  Raw Event Logs │
└────────┬────────┘
         │
         ↓
┌─────────────────┐
│  Data Loader    │  ← Load & validate CSV files
└────────┬────────┘
         │
         ↓
┌─────────────────┐
│  Preprocessor   │  ← Feature scaling (StandardScaler)
└────────┬────────┘
         │
         ↓
┌─────────────────┐
│  Neural Network │  ← Deep learning model
└────────┬────────┘
         │
         ↓
┌─────────────────┐
│  Threat Score   │  ← Probability + Classification
└─────────────────┘
```

---

## 📊 Dataset

**Source**: [BETH Dataset (Kaggle)](https://www.kaggle.com/datasets/katehighnam/beth-dataset)

**Research Paper**: [BETH Dataset: Real Cybersecurity Data for Anomaly Detection](https://www.gatsby.ucl.ac.uk/~balaji/udl2021/accepted-papers/UDL2021-paper-033.pdf)

### Features

| Feature | Description | Type |
|---------|-------------|------|
| `processId` | Unique identifier for the process | Integer |
| `threadId` | ID for the thread spawning the log | Integer |
| `parentProcessId` | Label for the parent process | Integer |
| `userId` | ID of user spawning the log | Integer |
| `mountNamespace` | Mounting restrictions | Integer |
| `argsNum` | Number of arguments passed | Integer |
| `returnValue` | Value returned from the event | Integer |
| **`sus_label`** | **Target: 0 = Benign, 1 = Threat** | **Binary** |

---

## ⚡ Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/yajatpawar24-beep/cyber-threat-detection.git
cd cyber-threat-detection

# Install dependencies
pip install -r requirements.txt

# Place your data files in data/raw/
# - labelled_train.csv
# - labelled_validation.csv
# - labelled_test.csv
```

### Training

```bash
# Train the model
python -m src.train

# Output:
# ✓ Model saved to models/model.pt
# ✓ Scaler saved to models/scaler.pkl
```

### Inference

```python
from src.predict import predict_threat

# Analyze a system event
is_threat, probability = predict_threat(
    processId=381,
    threadId=7337,
    parentProcessId=1,
    userId=100,
    mountNamespace=4026532231,
    argsNum=5,
    returnValue=0
)

print(f"Threat Detected: {is_threat}")
print(f"Confidence: {probability:.1%}")
```

**Output:**
```
Threat Detected: True
Confidence: 92.3%
```

---

## 📁 Project Structure

```
cyber-threat-detection/
├── src/
│   ├── __init__.py
│   ├── data_loader.py       # Data loading & validation
│   ├── preprocessor.py      # Feature engineering & scaling
│   ├── model.py             # Neural network architecture
│   ├── train.py             # Training pipeline
│   └── predict.py           # Inference engine
├── data/
│   └── raw/                 # CSV datasets
├── models/                  # Saved models & scalers
├── notebooks/               # Exploratory analysis
├── requirements.txt         # Python dependencies
└── README.md
```

---

### Training Configuration

- **Optimizer**: SGD with weight decay (0.0001)
- **Learning Rate**: 0.001
- **Loss Function**: Binary Cross-Entropy
- **Epochs**: 10 (default)
- **Batch Processing**: Full dataset per epoch

---

## 🔧 Technical Details

### Technologies Used

- **Framework**: PyTorch 2.0+
- **Data Processing**: Pandas, NumPy
- **Preprocessing**: Scikit-learn (StandardScaler)
- **Metrics**: TorchMetrics
- **Model Serialization**: PyTorch native + Joblib

### Key Design Decisions

1. **Binary Cross-Entropy Loss**: Appropriate for binary classification with sigmoid output
2. **StandardScaler**: Normalizes features for faster convergence
3. **Modular Architecture**: Separate concerns for maintainability
4. **Model Persistence**: Save both model weights and preprocessing pipeline

---

## 🛠️ Development

### Running Tests

```bash
# Test data loading
python -c "from src.data_loader import load_data; load_data()"

# Test model inference
python -m src.predict
```

### Customizing Training

Edit hyperparameters in `src/train.py`:

```python
train_model(
    num_epochs=50,        # Increase for better convergence
    learning_rate=0.001   # Adjust learning rate
)
```

---

## 🚀 Future Enhancements

- [ ] **API Deployment**: RESTful API with FastAPI for real-time predictions
- [ ] **Dockerization**: Containerize for easy deployment
- [ ] **Monitoring Dashboard**: Visualize threat patterns in real-time
- [ ] **Model Optimization**: Hyperparameter tuning with Optuna
- [ ] **Explainability**: Add SHAP values for feature importance
- [ ] **Batch Inference**: Process large log files efficiently
- [ ] **CI/CD Pipeline**: Automated testing and deployment

---

## 📚 Use Cases

This system can be integrated into:

- **Security Information and Event Management (SIEM)** systems
- **Intrusion Detection Systems (IDS)**
- **Security Operations Centers (SOC)** for automated triage
- **Cloud security platforms** for real-time threat monitoring
- **Endpoint Detection and Response (EDR)** solutions

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 👤 Author

**Yajat Pawar**

- GitHub: [@yajatpawar24-beep](https://github.com/yajatpawar24-beep)
- LinkedIn: [@YajatPawar](https://www.linkedin.com/in/yajat-pawar-47369337b/)
- Email: pawaryajat@gmail.com

---

## 🙏 Acknowledgments

- **BETH Dataset**: Kate Highnam et al. for providing the cybersecurity dataset
- **Research Paper**: [BETH Dataset: Real Cybersecurity Data for Anomaly Detection Research](https://www.gatsby.ucl.ac.uk/~balaji/udl2021/accepted-papers/UDL2021-paper-033.pdf)
- **Kaggle**: For hosting the dataset

---

## 📞 Support

If you found this project helpful, please consider:
- ⭐ Starring the repository
- 🐛 Reporting bugs via Issues
- 💡 Suggesting new features

---

<div align="center">

**Built with ❤️ for a safer digital world**

[⬆ back to top](#-cyber-threat-detection-system)

</div>
