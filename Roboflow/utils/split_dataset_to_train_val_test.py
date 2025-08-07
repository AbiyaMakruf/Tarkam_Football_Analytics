# Codingan untuk melakukan split dataset yang sudah dirubah dari format 4class menjadi 2class dengan persentase tertentu
import os
import random
import shutil

# Path awal
base_path = "train"
images_path = os.path.join(base_path, "images")
labels_path = os.path.join(base_path, "labels")

# Path output
output_base = "dataset"
splits = ['train', 'val', 'test']
ratios = [0.8, 0.15, 0.05]

# Buat folder output
for split in splits:
    os.makedirs(os.path.join(output_base, split, "images"), exist_ok=True)
    os.makedirs(os.path.join(output_base, split, "labels"), exist_ok=True)

# Ambil semua nama file tanpa ekstensi
image_files = [f for f in os.listdir(images_path) if f.endswith(('.jpg', '.png', '.jpeg'))]
random.shuffle(image_files)

# Hitung jumlah
n_total = len(image_files)
n_train = int(ratios[0] * n_total)
n_val = int(ratios[1] * n_total)
n_test = n_total - n_train - n_val

splits_files = {
    'train': image_files[:n_train],
    'val': image_files[n_train:n_train + n_val],
    'test': image_files[n_train + n_val:]
}

# Copy file image dan label
for split, files in splits_files.items():
    for img_file in files:
        label_file = os.path.splitext(img_file)[0] + ".txt"
        shutil.copy2(os.path.join(images_path, img_file), os.path.join(output_base, split, "images", img_file))
        shutil.copy2(os.path.join(labels_path, label_file), os.path.join(output_base, split, "labels", label_file))
