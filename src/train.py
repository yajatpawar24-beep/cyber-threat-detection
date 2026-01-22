import torch
import torch.nn as nn
import torch.optim as optim
from torchmetrics import Accuracy
import os

# Import from same directory
from src.data_loader import load_data
from src.preprocessor import preprocess_data
from src.model import CyberThreatDetector

def train_model(num_epochs=10, learning_rate=0.001):
    """Train the cyber threat detection model."""
    
    # Create models directory if it doesn't exist
    os.makedirs('models', exist_ok=True)
    
    # Set device
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    print(f"Using device: {device}")
    
    # Load data
    train_df, val_df, test_df = load_data()
    
    # Preprocess
    X_train, y_train, X_val, y_val, X_test, y_test, scaler = preprocess_data(
        train_df, val_df, test_df
    )
    
    # Convert to tensors
    X_train_tensor = torch.tensor(X_train, dtype=torch.float32).to(device)
    y_train_tensor = torch.tensor(y_train, dtype=torch.float32).view(-1, 1).to(device)
    X_val_tensor = torch.tensor(X_val, dtype=torch.float32).to(device)
    y_val_tensor = torch.tensor(y_val, dtype=torch.float32).view(-1, 1).to(device)
    X_test_tensor = torch.tensor(X_test, dtype=torch.float32).to(device)
    y_test_tensor = torch.tensor(y_test, dtype=torch.float32).view(-1, 1).to(device)
    
    # Create model
    model = CyberThreatDetector(input_size=X_train.shape[1]).to(device)
    
    # Loss and optimizer (FIXED: BCELoss instead of CrossEntropyLoss)
    criterion = nn.BCELoss()
    optimizer = optim.SGD(model.parameters(), lr=learning_rate, weight_decay=0.0001)
    
    # Training loop
    print(f"\nTraining for {num_epochs} epochs...")
    for epoch in range(num_epochs):
        model.train()
        optimizer.zero_grad()
        
        outputs = model(X_train_tensor)
        loss = criterion(outputs, y_train_tensor)
        
        loss.backward()
        optimizer.step()
        
        if (epoch + 1) % 5 == 0:
            print(f"Epoch [{epoch+1}/{num_epochs}], Loss: {loss.item():.4f}")
    
    # Evaluate
    model.eval()
    with torch.no_grad():
        y_predict_train = model(X_train_tensor).round()
        y_predict_test = model(X_test_tensor).round()
        y_predict_val = model(X_val_tensor).round()
    
    # Calculate accuracies
    accuracy = Accuracy(task="binary").to(device)
    
    train_accuracy = accuracy(y_predict_train, y_train_tensor).item()
    test_accuracy = accuracy(y_predict_test, y_test_tensor).item()
    val_accuracy = accuracy(y_predict_val, y_val_tensor).item()
    
    print(f"\n=== Results ===")
    print(f"Training accuracy: {train_accuracy:.4f}")
    print(f"Validation accuracy: {val_accuracy:.4f}")
    print(f"Testing accuracy: {test_accuracy:.4f}")
    
    # Save model
    torch.save(model.state_dict(), 'models/model.pt')
    print("\nSaved model to models/model.pt")
    
    return model

if __name__ == '__main__':
    train_model(num_epochs=10)