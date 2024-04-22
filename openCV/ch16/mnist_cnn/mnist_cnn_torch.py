# colab 에서 실행 할것!

import torch
import torch.nn as nn
import torch.onnx
import torch.optim as optim
from torch.utils.data import DataLoader
from torchvision import datasets, transforms

# 데이터셋 로드
mnist_train = datasets.MNIST(
    root="./mnist_data/", train=True, transform=transforms.ToTensor(), download=True
)

# 하이퍼파라미터
learning_rate = 0.001
training_epochs = 20
batch_size = 100

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(device)


# 모델 구성
class CNN(nn.Module):
    def __init__(self):
        super(CNN, self).__init__()
        self.layer1 = nn.Sequential(
            nn.Conv2d(1, 32, kernel_size=3, stride=1, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2, stride=2),
        )
        self.layer2 = nn.Sequential(
            nn.Conv2d(32, 64, kernel_size=3, stride=1, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2, stride=2),
        )
        self.fc1 = nn.Linear(7 * 7 * 64, 256, bias=True)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(256, 10, bias=True)
        torch.nn.init.xavier_uniform_(self.fc1.weight)
        torch.nn.init.xavier_uniform_(self.fc2.weight)

    def forward(self, x):
        out = self.layer1(x)
        out = self.layer2(out)
        out = out.view(out.size(0), -1)
        out = self.fc1(out)
        out = self.relu(out)
        out = self.fc2(out)
        return out


model = CNN().to(device)

# 손실 함수와 옵티마이저
criterion = nn.CrossEntropyLoss().to(device)
optimizer = optim.Adam(model.parameters(), lr=learning_rate)

# 데이터 로더
data_loader = DataLoader(dataset=mnist_train, batch_size=batch_size, shuffle=True)

# 훈련
for epoch in range(training_epochs):
    avg_cost = 0
    total_batch = len(data_loader)

    for X, Y in data_loader:
        X = X.view(-1, 1, 28, 28).to(device)
        Y = Y.to(device)

        optimizer.zero_grad()
        hypothesis = model(X)
        cost = criterion(hypothesis, Y)
        cost.backward()
        optimizer.step()

        avg_cost += cost / total_batch

    print("[Epoch: {:>4}] cost = {:>.9}".format(epoch + 1, avg_cost))

model.to("cpu")
dummy_input = torch.randn(1, 1, 28, 28)
torch.onnx.export(model, dummy_input, "mnist_cnn.onnx")

print("Learning finished!")

# !pip install onnx
