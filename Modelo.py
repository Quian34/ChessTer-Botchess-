
#Red neuronal base
import torch.nn as nn


class QueenCrow_bot(nn.Module):
    def __init__(self, n_class):
        super(QueenCrow_bot, self).__init__()
        #c1 -> rel -> c2 -> rel -> flat -> f1 -> rel -> f2

        #Conv2d que transforma 13 canales a 64 
        #Con kernel 3x3 y padding 1 (mantiene tamaño 8x8).
        self.c1 = nn.Conv2d(13, 64, kernel_size=3, padding=1)
        #Conv2d que transforma 64 canales a 128, mismo kernel y padding.
        self.c2 = nn.Conv2d(64, 128, kernel_size=3, padding=1)
        self.flat = nn.Flatten()
        #Reduce las 8192 características a 256.
        self.f1 = nn.Linear(8 * 8 * 128, 256) # 128 canales correctos
        #Reduce de 256 a n_class (posibles movimientos)
        self.f2 = nn.Linear(256, n_class)
        self.relu = nn.ReLU() #Para no linealidad

        #Peso Jugadas
        nn.init.kaiming_uniform_(self.c1.weight, nonlinearity='relu')
        nn.init.kaiming_uniform_(self.c2.weight, nonlinearity='relu')
        nn.init.xavier_uniform_(self.f1.weight)
        nn.init.xavier_uniform_(self.f2.weight)

#Output layers -> Probabilidades
    def forward(self, x):
        x = self.relu(self.c1(x))
        x = self.relu(self.c2(x))
        x = self.flat(x)
        x = self.relu(self.f1(x))
        x = self.f2(x) # Suelta lógica cruda
        return x
