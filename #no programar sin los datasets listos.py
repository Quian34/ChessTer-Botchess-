#no programar sin los datasets listos
#Bases, bocetos, ejemplos, referencias


#Lectura de datos pgn
files = [file for
 file in
  os.listir("data/pgn)") if file.endswith(".pgn")]

from chess import pgn
def load_pgo(file_path):
    games = []
        with open(file_path, 'r') as pgn_file:
            while True:
                game = pgn.read_game(pgn_file)
                if game is None:
                    Break #Rompe el ciclo
                games.append(game)
return games

LIMIT_FILES = min(len(files), 24)
games = []
i=1
for file in tqdm(files):
    games.extend(load_pgn(f"data/pgn/(file,"))
    if ( i >= LIMIT_FILES):
        break
    i += 1

    len(games)

    # Neural network "Just a scratch"
    class Model(nn.Module):
        def __init__(self):
            super().__init__(self):
            self.conv1 = nn.Conv2d(1, 20, 5)
            self.conv2 = nn.Conv2d (20, 20, 5)

        def forward(self, x):
            x=F.relu(self.conv1(x))
            return F.relu(self.conv2(x))