# Codingan untuk menampilkan gambar dengan bounding box dari dataset YOLO format.

import os
import cv2

# Path folder
image_dir = 'dataset_yolo_format/test/images'
label_dir = 'dataset_yolo_format/test/labels'

# Kelas untuk tampilan
class_names = ['player', 'ball', 'referee', 'goalkeeper']
colors = [(0,255,0), (0,0,255), (255,0,0), (0,255,255)]

# Loop setiap gambar
for fname in sorted(os.listdir(image_dir)):
    if not fname.endswith('.jpg'):
        continue

    img_path = os.path.join(image_dir, fname)
    label_path = os.path.join(label_dir, fname.replace('.jpg', '.txt'))

    img = cv2.imread(img_path)
    H, W = img.shape[:2]

    if os.path.exists(label_path):
        with open(label_path, 'r') as f:
            for line in f:
                parts = line.strip().split()
                cls_id = int(parts[0])
                xc, yc, w, h = map(float, parts[1:])

                x1 = int((xc - w/2) * W)
                y1 = int((yc - h/2) * H)
                x2 = int((xc + w/2) * W)
                y2 = int((yc + h/2) * H)

                color = colors[cls_id]
                cv2.rectangle(img, (x1, y1), (x2, y2), color, 2)
                cv2.putText(img, class_names[cls_id], (x1, y1 - 5),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 1)

    cv2.imshow('YOLO BBoxes', img)
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
