# Codingan untuk menampilkan gambar dan bounding box dari dataset yang masih menggunakan format original dari SoccerNet.

import cv2
import os
import pandas as pd

# Path ke folder
base_path = 'dataset/test/SNMOT-117'
img_path = os.path.join(base_path, 'img1')
gt_path = os.path.join(base_path, 'gt', 'gt.txt')

# Load anotasi ground truth
cols = ['frame', 'track_id', 'x', 'y', 'w', 'h', 'conf', 'class', 'vis', 'dummy']
gt = pd.read_csv(gt_path, header=None, names=cols)

# Loop untuk menampilkan gambar + bbox
frame_ids = sorted(gt['frame'].unique())
for frame_id in frame_ids:
    frame_file = f"{frame_id:06}.jpg"
    full_path = os.path.join(img_path, frame_file)
    
    if not os.path.exists(full_path):
        continue

    img = cv2.imread(full_path)
    frame_data = gt[gt['frame'] == frame_id]

    for _, row in frame_data.iterrows():
        x1, y1, w, h = int(row['x']), int(row['y']), int(row['w']), int(row['h'])
        x2, y2 = x1 + w, y1 + h
        cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(img, f"ID {int(row['track_id'])}", (x1, y1 - 5),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)

    cv2.imshow('Frame', img)
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
