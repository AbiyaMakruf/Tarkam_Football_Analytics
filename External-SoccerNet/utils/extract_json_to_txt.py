import os
import json

json_file = 'labels.json'
output_dir = 'restored_labels'
os.makedirs(output_dir, exist_ok=True)

with open(json_file, 'r') as f:
    label_data = json.load(f)

for key, boxes in label_data.items():
    with open(os.path.join(output_dir, f"{key}.txt"), 'w') as f:
        for box in boxes:
            line = ' '.join(map(str, box))
            f.write(line + '\n')

print(f"✅ Label berhasil di-extract ke folder: {output_dir}")
