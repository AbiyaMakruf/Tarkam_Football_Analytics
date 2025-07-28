import os
import json

label_dir = 'dataset_yolo_format/valid/labels'
output_json = 'dataset_yolo_format/valid/labels.json'

label_data = {}

for fname in os.listdir(label_dir):
    if fname.endswith('.txt'):
        key = fname.replace('.txt', '')
        with open(os.path.join(label_dir, fname), 'r') as f:
            lines = f.read().strip().split('\n')
            bboxes = [list(map(float, line.split())) for line in lines if line]
            label_data[key] = bboxes

with open(output_json, 'w') as f:
    json.dump(label_data, f)

print(f"✅ {len(label_data)} label berhasil disatukan ke {output_json}")
