import torch

#Nota, este dataset solo funciona bien en matrices
#El tablero es reconocido como una matriz 8x8 (0-7)
class ChessTerDt(Dataset):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __len__(self):
        return len(self.x)
    
    def __getitem__(self, idx):
        return self.x[idx], self.y[idy]