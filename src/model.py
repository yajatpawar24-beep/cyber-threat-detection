import torch
import torch.nn as nn

class CyberThreatDetector(nn.Module):
    """Neural network for detecting cyber threats."""
    
    def __init__(self, input_size):
        super(CyberThreatDetector, self).__init__()
        
        self.network = nn.Sequential(
            nn.Linear(input_size, 128),
            nn.ReLU(),
            nn.Linear(128, 64),
            nn.ReLU(),
            nn.Linear(64, 1),
            nn.Sigmoid()
        )
    
    def forward(self, x):
        return self.network(x)