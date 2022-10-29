import torch
import torchvision
from torchvision import transforms, datasets
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import numpy as np
from torch.utils.data import TensorDataset, DataLoader
import math
from training.model import Net



def run_test(modelPath, xPath, yPath):
    test_x = np.load(xPath)
    test_y = np.load(yPath)
    print(test_x.shape)
    print(test_y.shape)

    tensor_x = torch.Tensor(test_x)
    tensor_y = torch.Tensor(test_y)

    testSet = TensorDataset(tensor_x, tensor_y)
    testLoader = DataLoader(testSet, batch_size=1, shuffle=True)

    net = Net()
    net.load_state_dict(torch.load(modelPath))

    loss_fnc = nn.MSELoss()
    with torch.no_grad():
        running_loss = 0.0
        count = 0
        for data in testLoader:
            X, y = data
            output = net(X)
            loss = loss_fnc(output, y.unsqueeze(1))
            running_loss += loss.item()
            count += 1
            if count % 10000 == 0:
                print(count)
            # print(loss.item())
        print("Average Loss:", running_loss/count)
    
# run_test("models/1665154011re", "numpy/basic_test_x.npy", "numpy/basic_test_y.npy")