import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader, WeightedRandomSampler
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import csv
from Fight import FightsDataset
from tqdm import tqdm

INPUT_FILE = "ufc_fight_outcomes.csv"


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

def train(model, train_loader, optimizer, loss_function):
    model.train()
    loss_sum = 0
    for idx, sample in enumerate(train_loader):
        data = sample['data']
        truth = sample['truth']

        optimizer.zero_grad()
        out = model(data)
        
        loss = loss_function(out, truth)

        loss.backward()
        optimizer.step()
        loss_sum+= loss.item()


    #print("Training Loss : {:.1f}".format(loss_sum))
    return out
def test(model, testSet, loss_function):
    model.eval()
    numCorrect, total = 0,0
    with torch.no_grad():
        for sample in testSet:
            data = sample['data']
            truth = sample['truth']

            print(data)
            out = model(data)
            out = out.round()

            for prediction, label in zip(out, truth):
                if prediction == label:
                    
                    numCorrect+=1
                total+=1
        print("Test Accuracy = {:.1f}%".format((numCorrect/total)*100))

fights_data = FightsDataset(INPUT_FILE)
training, testing  = [], []
training, testing = torch.utils.data.random_split(fights_data, [len(fights_data)-500, 500])
print("Training set size = {} | Testing set size = {}".format(len(training),len(testing)))

train_loader = DataLoader(training, batch_size=100, shuffle = True)
test_loader = DataLoader(testing, batch_size=100, shuffle = False)

model = FNN(hidden_layers=500)
loss_function = nn.BCELoss()
optimizer = optim.Adam(model.parameters(), lr = 0.001)
epochs = 30
out = None
for epoch in (range(epochs)):
    #print(list(model.parameters()))how to 
    out = train(model, train_loader, optimizer, loss_function)
    if epoch % 5 == 0:
        test(model, test_loader, loss_function)
        for i in optimizer.param_groups:
            i['lr'] /= 2

print("saving model...")
torch.save(model.state_dict(), "UFC_Judge.pt")
    

