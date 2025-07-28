# Codingan ini digunakan untuk membagi dataset YOLO format menjadi train dan valid set.

import os
import random
from shutil import move
from pathlib import Path

# Path awal dan tujuan
base_path = 'dataset_yolo_format'
src_img_dir = os.path.join(base_path, 'train/images')
src_lbl_dir = os.path.join(base_path, 'train/labels')

train_img_out = os.path.join(base_path, 'train/images')
train_lbl_out = os.path.join(base_path, 'train/labels')

valid_img_out = os.path.join(base_path, 'valid/images')
valid_lbl_out = os.path.join(base_path, 'valid/labels')

# Buat folder valid jika belum ada
os.makedirs(valid_img_out, exist_ok=True)
os.makedirs(valid_lbl_out, exist_ok=True)

# Persentase split
train_ratio = 0.9

# Ambil semua file .jpg
all_images = sorted([f for f in os.listdir(src_img_dir) if f.endswith('.jpg')])

# Hitung batas split
split_idx = int(len(all_images) * train_ratio)
train_set = all_images[:split_idx]
valid_set = all_images[split_idx:]

# Fungsi pindah gambar dan label
def move_pair(file_list, dst_img_dir, dst_lbl_dir):
    for img_name in file_list:
        lbl_name = img_name.replace('.jpg', '.txt')

        move(os.path.join(src_img_dir, img_name), os.path.join(dst_img_dir, img_name))
        if os.path.exists(os.path.join(src_lbl_dir, lbl_name)):
            move(os.path.join(src_lbl_dir, lbl_name), os.path.join(dst_lbl_dir, lbl_name))

# Pindahkan data ke folder valid
move_pair(valid_set, valid_img_out, valid_lbl_out)

print(f"✅ Split selesai. Total gambar: {len(all_images)} | Train: {len(train_set)} | Valid: {len(valid_set)}")

