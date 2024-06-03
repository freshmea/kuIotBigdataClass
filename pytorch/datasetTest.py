import pandas as pd
import torch
from torch.utils.data import DataLoader, Dataset


class MyDataset(Dataset):
    def __init__(self, csv_file):
        self.label = pd.read_csv(csv_file)
    
    def __len__(self):
        return len(self.label)
    
    def __getitem__(self, idx):
        sample = torch.tensor(self.label.iloc[idx, 0:3]).int()
        label = torch.tensor(self.label.iloc[idx, 3]).int()
        return sample, label

def main():
    folder = "/home/aa/kuIotBigdataClass/pytorch/data/"
    tensor_dataset = MyDataset(folder +"covtype.csv")
    dataset = DataLoader(tensor_dataset, batch_size=100, shuffle=True)
    
    for i, (sample, label) in enumerate(dataset):
        print(f"sample : {sample}")
        print(f"label : {label}")

if __name__ == "__main__":
    main()
