import torch
import pandas as pd
import joblib
from src.model import CyberThreatDetector

def load_model():
    """Load the trained model and scaler."""
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    
    # Load model
    model = CyberThreatDetector(input_size=7)
    model.load_state_dict(torch.load('models/model.pt', map_location=device))
    model.to(device)
    model.eval()
    
    # Load scaler
    scaler = joblib.load('models/scaler.pkl')
    
    return model, scaler, device

def predict_threat(processId, threadId, parentProcessId, userId, 
                   mountNamespace, argsNum, returnValue):
    """Predict if an event is a threat.
    
    Example:
        is_threat, probability = predict_threat(381, 7337, 1, 100, 4026532231, 5, 0)
    """
    model, scaler, device = load_model()
    
    # Create dataframe
    event = pd.DataFrame([[processId, threadId, parentProcessId, userId, 
                          mountNamespace, argsNum, returnValue]])
    
    # Scale
    event_scaled = scaler.transform(event)
    
    # Convert to tensor
    event_tensor = torch.tensor(event_scaled, dtype=torch.float32).to(device)
    
    # Predict
    with torch.no_grad():
        probability = model(event_tensor).item()
        prediction = 1 if probability > 0.5 else 0
    
    return prediction, probability

if __name__ == '__main__':
    # Example prediction
    is_threat, prob = predict_threat(
        processId=381,
        threadId=7337,
        parentProcessId=1,
        userId=100,
        mountNamespace=4026532231,
        argsNum=5,
        returnValue=0
    )
    
    print(f"Threat: {is_threat}, Probability: {prob:.4f}")