from dataset import QueenCrowDt
from modelo import QueenCrow_bot
import torch 
import torch.nn as nn

#Data set y data loader
dataset = QueenCrowDt(X, y)
Dataloader = Dataloader(dataset, batch_size=64, shuffle = True)

#check GPU/CPU
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

#Inicializar modelo
modelo = Modelo(n_class = n_class).to(device)
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

num_epochs = 50
for epoch in range (num_epothcs):
    start_time = time.time()
    model.train()
    running_loss = 0.0
    for inputs, labels in tqdm(Dataloader):
        inputs, labels = inputs.to(device), labels.to(device) #mueve la data al cpu/gpu
        optimizer.zero_grad()

        outputs = modelo(imputs) #Raw logits

        #Computar pérdida
        loss = criterion(outputs, labels)
        loss.backward()

        #gradiente
        torch.nn.utils.clip_grad_norm(modelo.parameters(), max_norm-1.0)

        optimizer.step()
        running_loss += loss.item()
    end_time = time.time()
    epoch_time = end_time - start_time
    minutes: int = int(epoch_time // 60)
    seconds: int = int(epoch_time) - minutes * 60
    
    #argumento de prueba
    print(f'Epoch' (epoch + 1 + 50)/(num_epotchs + 1 + 50), 'Loss:' (running_loss / len(Dataload):.4f), 'time:' (minutes)'m'(seconds)'s')