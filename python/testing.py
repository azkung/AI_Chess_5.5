# from tools import board_to_np, square_to_row_col
# import chess
# import torch
# import torch.nn as nn
# from training.model import Net
# import random
# import os
# import numpy as np
# import bots.bot_middle as bot_middle
# import bots.bot_middle_new as bot_middle_new
# import bots.bot_net_traversal as bot_net_traversal
# import bots.bot_net_traversal_2 as bot_net_traversal_2 
# import bots.bot_attack as bot_attack 
import bots.bot_basic as bot_basic 
# import bots.bot_custom as bot_custom 
import time
import chess
# import bots.bot_middle_new as bot_middle_new

# b = chess.Board('8/1Q1bbkpr/4pn2/7p/4PP2/1N4P1/Pq1BB2P/R4RK1 b - - 0 30')

b = chess.Board()

print(b)

s = time.perf_counter()
m = bot_basic.bestMove(b)
b.push(m)
e = time.perf_counter()
print(b)
print(e-s)


# for s in chess.SQUARES:
#     print(s, b.piece_at(s))

# WHITE_MODEL_PATH = os.path.dirname(os.path.realpath(__file__)) + '/models/WhitePieceSelector'
# BLACK_MODEL_PATH = os.path.dirname(os.path.realpath(__file__)) + '/models/BlackPieceSelector'

# whiteNet = Net()
# whiteNet.load_state_dict(torch.load(WHITE_MODEL_PATH))
# device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')

# print(b)
# print()
# print(chess.C6 in b.attacks(chess.C8))

# print(b)

# s = time.perf_counter()
# x = board_to_np(b)
# x = torch.Tensor(x)
# y = whiteNet(x.unsqueeze(0))
# y = torch.argsort(y, descending=True)
# en = enumerate(y[0])
# print(en)
# d_old = dict(en)
# d = dict((chess.SQUARE_NAMES[v.item()],k) for k,v in d_old.items())
# e = time.perf_counter()
# print(e-s)
# print(chess.SQUARE_NAMES[1])


# s = time.perf_counter()
# bot_custom.bestMove(b)
# e = time.perf_counter()
# print(e-s)

# s = time.perf_counter()
# bot_middle_new.bestMove(b)
# e = time.perf_counter()
# print(e-s)

# s = time.perf_counter()
# bot_basic.scoreCalcBoard(b)
# e = time.perf_counter()
# print(e-s)

# s = time.perf_counter()
# x = board_to_np(b)
# x = torch.Tensor(x)
# x = x.unsqueeze(0)
# # y = whiteNet(x)
# e = time.perf_counter()
# print(e-s)

# s2 = time.perf_counter()
# bot_middle.bestMove(b)
# e2 = time.perf_counter()


# print(e1-s1)
# print(e2-s2)

# s2 = time.perf_counter()
# x = board_to_np(b)
# x = torch.Tensor(x)
# y = whiteNet(x.unsqueeze(0))
# y = torch.argsort(y, descending=True)
# e2 = time.perf_counter()
# print(e2-s2)


# print(b)

# # train_x = np.load(os.path.dirname(os.path.realpath(__file__)) + "/numpy/training/1666364908_x.npy")
# # print(train_x.shape)
# WHITE_MODEL_PATH = os.path.dirname(os.path.realpath(__file__)) + '/models/WhitePieceSelector'
# BLACK_MODEL_PATH = os.path.dirname(os.path.realpath(__file__)) + '/models/BlackPieceSelector'

# whiteNet = Net()
# blackNet = Net()

# whiteNet.load_state_dict(torch.load(WHITE_MODEL_PATH))
# blackNet.load_state_dict(torch.load(BLACK_MODEL_PATH))

# x = board_to_np(b)
# x = torch.Tensor(x)
# y = whiteNet(x.unsqueeze(0))
# y = torch.argsort(y, descending=True)
# print(y)
# for i, a in enumerate(y[0]):
#     print(a.item(), square_to_row_col(a.item()), len(b.attacks(a.item())))
#     break

# b.push_san('e3')
# print(b)

# x = board_to_np(b)
# x = torch.Tensor(x)
# y = blackNet(x.unsqueeze(0))
# y = torch.argsort(y, descending=True)
# print(y)
# for i, a in enumerate(y[0]):
#     print(a.item(), square_to_row_col(a.item()), len(b.attacks(a.item())))
#     break




# net.load_state_dict(torch.load(MODEL_PATH))

# x = board_to_np(b)
# x = torch.Tensor(x)
# x = x.unsqueeze(0)
# y = net(x)
# # _, predicted = torch.max(y, 1)

# # print('Predicted: ', ' '.join(f'{predicted[j]}'
# #                               for j in range(1)))
# f = nn.Softmax(dim=1)
# y = f(y)
# # y = y.reshape((8,8))
# # print(y.shape)
# print(y)
# print(torch.argmax(y))
# print(torch.argsort(y))
# y = torch.argsort(y, descending=True)
# for i, x in enumerate(y[0]):
#     print(x.item(), square_to_row_col(x.item()))

# b.push_san('e3')
# print(b)
# b.push_san('e6')
# print(b)

# x = board_to_np(b)
# x = torch.Tensor(x)
# x = x.unsqueeze(0)
# y = net(x)
# y = f(y)
# print(y)
# print(torch.argmax(y))
# print(torch.argsort(y))
# y = torch.argsort(y, descending=True)
# for i, x in enumerate(y[0]):
#     print(x.item(), square_to_row_col(x.item()))

# # b.push_san("d3")
# print(b)
# x = board_to_np(b)
# x = torch.Tensor(x)
# x = x.unsqueeze(0)
# y = net(x)
# y = y.reshape((8,8))
# print(y.shape)
# print(y)

# x = x[None]
# x = torch.Tensor(x)
# print(x.shape)
# x1 = torch.Tensor(x[0])
# x2 = torch.Tensor(x[1])
# print(x1[None].shape)
# print(x2[None].shape)
# net = Net()

# print(chess.SQUARES)

# for square in chess.SQUARES:
#     print(b.piece_at(square))

# print(b)

# for move in b.legal_moves:
#     aa = move_to_np(move)
#     print(move)
#     print(aa)


# b.push(random.sample(list(b.legal_moves),1)[0])

# for move in b.legal_moves:
#     aa = move_to_np(move)
#     print(move)
#     print(aa)
    
# for move in b.legal_moves:
#     print(move.from_square, move)

# with torch.no_grad():
#     print(net(x))

# with open("datasets/ficsgamesdb_2021_standard2000_nomovetimes_264388.pgn") as pgn:
#     x = []
#     y = []
#     game = chess.pgn.read_game(pgn)
#     count = 0
#     while game != None:
#         game = chess.pgn.read_game(pgn)
#         count += 1
#         print(count)
# import torch
# import torchvision
# import torchvision.transforms as transforms

# transform = transforms.Compose(
#     [transforms.ToTensor(),
#      transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])

# batch_size = 4

# trainset = torchvision.datasets.CIFAR10(root='./data', train=True,
#                                         download=True, transform=transform)
# trainloader = torch.utils.data.DataLoader(trainset, batch_size=batch_size,
#                                           shuffle=True, num_workers=2)

# testset = torchvision.datasets.CIFAR10(root='./data', train=False,
#                                        download=True, transform=transform)
# testloader = torch.utils.data.DataLoader(testset, batch_size=batch_size,
#                                          shuffle=False, num_workers=2)

# classes = ('plane', 'car', 'bird', 'cat',
#            'deer', 'dog', 'frog', 'horse', 'ship', 'truck')

# import torch.nn as nn
# import torch.nn.functional as F


# class Net(nn.Module):
#     def __init__(self):
#         super().__init__()
#         self.conv1 = nn.Conv2d(3, 6, 5)
#         self.pool = nn.MaxPool2d(2, 2)
#         self.conv2 = nn.Conv2d(6, 16, 5)
#         self.fc1 = nn.Linear(16 * 5 * 5, 120)
#         self.fc2 = nn.Linear(120, 84)
#         self.fc3 = nn.Linear(84, 10)

#     def forward(self, x):
#         x = self.pool(F.relu(self.conv1(x)))
#         x = self.pool(F.relu(self.conv2(x)))
#         x = torch.flatten(x, 1) # flatten all dimensions except batch
#         x = F.relu(self.fc1(x))
#         x = F.relu(self.fc2(x))
#         x = self.fc3(x)
#         return x


# net = Net()

# import torch.optim as optim

# criterion = nn.CrossEntropyLoss()
# optimizer = optim.SGD(net.parameters(), lr=0.001, momentum=0.9)

# for epoch in range(2):  # loop over the dataset multiple times

#     running_loss = 0.0
#     for i, data in enumerate(trainloader, 0):
#         # get the inputs; data is a list of [inputs, labels]
#         inputs, labels = data
#         print(inputs.shape)

#         # zero the parameter gradients
#         optimizer.zero_grad()

#         # forward + backward + optimize
#         outputs = net(inputs)
#         loss = criterion(outputs, labels)
#         loss.backward()
#         optimizer.step()

#         # print statistics
#         running_loss += loss.item()
#         if i % 2000 == 1999:    # print every 2000 mini-batches
#             print(f'[{epoch + 1}, {i + 1:5d}] loss: {running_loss / 2000:.3f}')
#             running_loss = 0.0

# print('Finished Training')