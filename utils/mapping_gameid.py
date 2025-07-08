# Codingan untuk melakukan mapping gameID sehingga memudahkan untuk mengetahui folder X memiliki gameID berapa.

import os
from collections import defaultdict

# Folder train
# root_dir = 'dataset/train'
# output_file = 'mapping_gameID_train.txt'

# Folder test
root_dir = 'dataset/test'
output_file = 'mapping_gameID_test.txt'

gameid_map = defaultdict(list)

# Telusuri setiap subfolder dalam dataset/test
for folder in os.listdir(root_dir):
    folder_path = os.path.join(root_dir, folder)
    if os.path.isdir(folder_path):
        ini_path = os.path.join(folder_path, 'gameinfo.ini')
        if os.path.exists(ini_path):
            with open(ini_path, 'r') as f:
                for line in f:
                    if line.startswith('gameID='):
                        game_id = line.strip().split('=')[1]
                        gameid_map[game_id].append(folder)
                        break

# Simpan hasil mapping ke file txt
with open(output_file, 'w') as f:
    for game_id, folders in sorted(gameid_map.items(), key=lambda x: int(x[0])):
        sorted_folders = sorted(folders, key=lambda name: int(name.split('-')[1]))
        f.write(f'gameID{game_id}: {", ".join(sorted_folders)}\n')

