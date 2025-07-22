#Codingan untuk membagi dataset YOLO format menjadi 5000 file total (custom split)

import os
import shutil

# ===============================
# Konfigurasi
# ===============================
SOURCE_ROOT = 'dataset_yolo_format'
OUTPUT_ROOT = 'dataset_yolo_format_split/5000'
MAX_TOTAL = 5000
SPLIT_PORTION = {
    'train': 0.7,  # dari dataset_yolo_format/train
    'valid': 0.2,  # dari dataset_yolo_format/valid
    'test':  0.1   # dari dataset_yolo_format/test
}
# ===============================

def sample_and_copy(src_split, dst_split, max_n):
    src_img = os.path.join(SOURCE_ROOT, src_split, 'images')
    src_lbl = os.path.join(SOURCE_ROOT, src_split, 'labels')
    dst_img = os.path.join(OUTPUT_ROOT, dst_split, 'images')
    dst_lbl = os.path.join(OUTPUT_ROOT, dst_split, 'labels')

    os.makedirs(dst_img, exist_ok=True)
    os.makedirs(dst_lbl, exist_ok=True)

    all_images = sorted([f for f in os.listdir(src_img) if f.endswith('.jpg')])
    selected = all_images[:max_n]

    for img_name in selected:
        lbl_name = img_name.replace('.jpg', '.txt')

        shutil.copy2(os.path.join(src_img, img_name), os.path.join(dst_img, img_name))
        if os.path.exists(os.path.join(src_lbl, lbl_name)):
            shutil.copy2(os.path.join(src_lbl, lbl_name), os.path.join(dst_lbl, lbl_name))

    return len(selected)

# Hitung jumlah file masing-masing
n_train = int(MAX_TOTAL * SPLIT_PORTION['train'])
n_valid = int(MAX_TOTAL * SPLIT_PORTION['valid'])
n_test  = MAX_TOTAL - n_train - n_valid

# Jalankan pemindahan
count_train = sample_and_copy('train', 'train', n_train)
count_valid = sample_and_copy('valid', 'valid', n_valid)
count_test  = sample_and_copy('test', 'test', n_test)

print(f"✅ Sampling selesai. Total {count_train + count_valid + count_test} file:")
print(f" - Train : {count_train}")
print(f" - Valid : {count_valid}")
print(f" - Test  : {count_test}")
