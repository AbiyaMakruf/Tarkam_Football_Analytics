# Codingan untuk mengonversi ground truth dari dataset MOT ke format YOLO.

import os
import cv2
import pandas as pd
from shutil import copy2

# Path utama
source_root = 'dataset/test'
output_root = 'dataset_yolo_format/test'
image_out = os.path.join(output_root, 'images')
label_out = os.path.join(output_root, 'labels')

os.makedirs(image_out, exist_ok=True)
os.makedirs(label_out, exist_ok=True)

# Mapping kelas
label2id = {'player': 0, 'ball': 1, 'referee': 2, 'goalkeeper': 3}

# Loop semua folder di dalam dataset/train/
for folder in sorted(os.listdir(source_root)):
    folder_path = os.path.join(source_root, folder)
    if not os.path.isdir(folder_path):
        continue

    # Load gameinfo.ini → mapping trackletID ke kelas
    tracklet_map = {}
    info_path = os.path.join(folder_path, 'gameinfo.ini')
    with open(info_path, 'r') as f:
        for line in f:
            if line.startswith('trackletID_'):
                parts = line.strip().split('=')
                track_id = int(parts[0].split('_')[1])
                obj_type = parts[1].split(';')[0].strip()

                if obj_type.startswith('player'):
                    label = 'player'
                elif obj_type.startswith('referee'):
                    label = 'referee'
                elif obj_type.startswith('ball'):
                    label = 'ball'
                elif obj_type.startswith('goalkeeper'):
                    label = 'goalkeeper'
                else:
                    continue
                tracklet_map[track_id] = label

    # Baca groundtruth
    gt_path = os.path.join(folder_path, 'gt', 'gt.txt')
    cols = ['frame', 'track_id', 'x', 'y', 'w', 'h', 'conf', 'class', 'vis', 'dummy']
    gt = pd.read_csv(gt_path, header=None, names=cols)

    # Path gambar
    img_path = os.path.join(folder_path, 'img1')

    # Loop semua frame
    for frame_id, rows in gt.groupby('frame'):
        frame_file = f"{int(frame_id):06}.jpg"
        full_img_path = os.path.join(img_path, frame_file)

        if not os.path.exists(full_img_path):
            continue

        # Read image untuk ukuran
        img = cv2.imread(full_img_path)
        H, W = img.shape[:2]

        # Buat label YOLO
        yolo_labels = []
        for _, row in rows.iterrows():
            track_id = int(row['track_id'])
            if track_id not in tracklet_map:
                continue
            cls_name = tracklet_map[track_id]
            cls_id = label2id[cls_name]

            xc = (row['x'] + row['w']/2) / W
            yc = (row['y'] + row['h']/2) / H
            ww = row['w'] / W
            hh = row['h'] / H

            yolo_labels.append(f"{cls_id} {xc:.6f} {yc:.6f} {ww:.6f} {hh:.6f}")

        # Nama unik: SNMOT-060_000001.jpg
        new_name = f"{folder}_{int(frame_id):06}"

        # Simpan label
        if yolo_labels:
            with open(os.path.join(label_out, new_name + '.txt'), 'w') as f:
                f.write('\n'.join(yolo_labels))

        # Copy gambar
        copy2(full_img_path, os.path.join(image_out, new_name + '.jpg'))

print("✅ Konversi selesai. Format YOLO tersimpan di dataset_yolo_format/test/")
