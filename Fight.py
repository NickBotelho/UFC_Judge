import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader, WeightedRandomSampler
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import csv
import random
import copy

#"Fight Outcome","Name","Knockdowns","Strikes","Takedowns","Submission Attempts","Weight Class","Title Fight","Outcome Method","Number of Rounds"
#0,2,3,4,5

class FightsDataset(Dataset):
    def __init__(self, fights):
        super().__init__()
        self.fight_history = pd.read_csv(fights, ",")
        print(self.fight_history.head())
        self.fight_history = self.fight_history[["Fight Outcome","Knockdowns","Strikes","Takedowns","Submission Attempts"]]
        print(self.fight_history.head())

        self.samples = self.divideSamples()
        print(len(self.samples))
    def divideSamples(self):
        samples = []
        for row in range(1, len(self.fight_history), 2):
            red = self.fight_history.iloc[row-1:row].to_numpy().tolist()
            blue = self.fight_history.iloc[row:row+1].to_numpy().tolist()

            red, blue = red[0], blue[0]

            for i in range(len(red)):
                r, b = int(red[i]), int(blue[i])
                r, b = self.normalize(r, b)
                red[i] = r
                blue[i] = b
            red = red[1:]
            blue = blue[1:]
            red_sample, blue_sample = {}, {}
            red_truth, blue_truth = 1, 0
            red_sample["data"] = torch.FloatTensor(red)
            red_sample['truth'] = torch.tensor(red_truth,dtype = torch.float32)
            blue_sample["data"] = torch.FloatTensor(blue)
            blue_sample['truth'] = torch.tensor(blue_truth,dtype = torch.float32)
            samples.append(copy.deepcopy(red_sample))
            samples.append(copy.deepcopy(blue_sample)) 
        return samples
    def divideSamples2(self):
        samples = []
        for row in range(1, len(self.fight_history), 2):
            red = self.fight_history.iloc[row-1:row].to_numpy().tolist()
            blue = self.fight_history.iloc[row:row+1].to_numpy().tolist()
            #print(red, blue)
            red, blue = red[0], blue[0]
            #print(red, blue)
            for i in range(len(red)):
                r, b = int(red[i]), int(blue[i])
                r, b = self.normalize(r, b)
                red[i] = r
                blue[i] = b
            red = red[1:]
            blue = blue[1:]
            sample = []
            first = random.randint(0,1)
            if first == 1:
                sample.append(blue)
                sample.append(red)
                truth = 1
            else:
                sample.append(red)
                sample.append(blue)
                truth = 0
            batch = {}
            batch['data'] = torch.FloatTensor(sample)
            batch['truth'] = torch.tensor(truth,dtype = torch.float32)
            samples.append(copy.deepcopy(batch))
        return samples

    def normalize(self, num1, num2):
        if num1 == 0 and num2 == 0:
            return [0,0]
        if num1 != 0 and num2 != 0:
            if num1 > num2:
                norm2 = num2/num1
                norm1 = 1
            else:
                norm1 = num1/num2
                norm2 = 1
        else:
            if num1 == 0:
                norm1, norm2 = 0, 1
            else:
                norm1, norm2 = 1, 0

        return [norm1, norm2]
    def __getitem__(self, index):
        return self.samples[index]
    def __len__(self):
        return len(self.samples)
            





