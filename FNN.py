import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader, WeightedRandomSampler

#"Fight Outcome","Name","Knockdowns","Strikes","Takedowns","Submission Attempts","Weight Class","Title Fight","Outcome Method","Number of Rounds"
#Data = 2,3,4,5 | Truth = 0 (Fight Outcome)

class FNN(nn.Module):
    def __init__(self, num_inputs = 4, num_outputs = 1, hidden_layers = 20):
        super(FNN, self).__init__()
        self.linear1 = nn.Linear(num_inputs, hidden_layers)
        self.linear2 = nn.Linear(hidden_layers, hidden_layers)
        self.linear3 = nn.Linear(hidden_layers, num_outputs)
        self.relu = nn.ReLU()
        self.softmax = nn.Softmax(dim = 1)

    def forward(self, x):

        x = torch.sigmoid(self.linear1(x))
        x = torch.sigmoid(self.linear2(x))
        x = torch.sigmoid(self.linear3(x))
        
        x = x.squeeze()

        #x = x[:,-1,:]

        return x