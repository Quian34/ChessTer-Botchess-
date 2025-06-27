#no programar sin los datasets listos
#¡Chess Engine with TensorFlow!


#Lectura de datos pgn
files = [file for file in os.listir("data/pgn)") if file.endswith(".pgn")]

from chess import pgn
def load-pgo(file_path):
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