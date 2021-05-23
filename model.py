import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader, WeightedRandomSampler
import numpy as np
import pandas as pd
from FNN import FNN

def GetWinnerPrediction(fighter1, fighter2):
    """Accepts 2 JSONs from the frontend and returns the predicted winner"""
    model = FNN(hidden_layers=500)
    model.load_state_dict(torch.load('UFC_Judge.pt'))
    red = parseData(fighter1)
    blue = parseData(fighter2)
    print(red, blue)
    for i in range(len(red)):
        r, b = int(red[i]), int(blue[i])
        r, b = normalize(r, b)
        red[i] = r
        blue[i] = b

    red_tensor = torch.FloatTensor(red)
    blue_tensor = torch.FloatTensor(blue)
    model.eval()
    output = model(red_tensor)
    output = output.round()
    if output == 1:
        return 'red'
    else:
        return 'blue'

# f1 = {
#     'kd': "23",
#     'name': "red",
#     'strikes': "2",
#     'sub': "3",
#     'td': "2"
# }
# f2 = {
#     'kd': "12",
#     'name': "blue",
#     'strikes': "3",
#     'sub': "3",
#     'td': "5"
# }
def parseData(fighter):
    res = []
    kd = 0 if fighter['kd'] == "" else fighter['kd']
    strikes = 0 if fighter['strikes'] == "" else fighter['strikes']
    sub = 0 if fighter['sub'] == "" else fighter['sub']
    td = 0 if fighter['td'] == "" else fighter['td']
    res.append(kd)
    res.append(strikes)
    res.append(sub)
    res.append(td)
    return res

def normalize(num1, num2):
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


