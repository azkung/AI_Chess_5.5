from nis import cat
import torch
import torchvision
from torchvision import transforms, datasets
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import numpy as np
from torch.utils.data import TensorDataset, DataLoader
import time
import chess

from tools import board_to_np


class Net(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = nn.Conv2d(6,1024,(3,3),stride=1,padding=1)
        self.conv2 = nn.Conv2d(1024,512,(3,3),stride=1,padding=1)
        self.fc1 = nn.Linear(32768, 2048)
        self.fc2 = nn.Linear(2048, 64)

    def forward(self, x):
        x = F.relu(self.conv1(x))
        x = F.relu(self.conv2(x))
        x = torch.flatten(x,1)
        x = F.relu(self.fc1(x))
        x = self.fc2(x)
        return x
