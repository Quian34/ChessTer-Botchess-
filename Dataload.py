from torch.utils.data import Dataloader

#Carga los archivos pgn
def load_pgn(file_path):
    games = []
    with open(file_path, 'r') as pgn_file:
        while True:
            game = pgn.read_game(pgn_file)
            if game is None:
                break
            games.append(game)
    return games

#Ruta archivos dataset
files = [file for file in os.listir("QueenCrow/Databases)") if file.endswith(".pgn")]
  File_Limit = min(len(files), 25)
  games = []
  i=1
  for file in tqdm(files):
    games.extend(load_pgn(f"QueenCrow/Databases/(file,"))
    if ( i >= LIMIT_FILES):
        break
    i += 1

    len(games)