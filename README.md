Jalankan Python utils/download_dataset.py dan tunggu hingga download selesai

Unzip folder train dan test dengan cara
unzip dataset/test.zip -d dataset/
unzip dataset/train.zip -d dataset/

Untuk mendapatkan mapping_gameID jalankan Python utils/mapping_gameid.py (Jalankan untuk folder train dan test dengan cara mengubah path nya)

Ubah format anotasi ground truth menjadi YOLO format dengan menjalankan Python utils/mapping_ground_truth_to_yolo_format.py (Jalankan untuk folder train dan test dengan cara mengubah path nya)

Didalam folder dataset_yolo_format buat file data.yaml yang isinya
```
train: ../train/images
val: ../valid/images
test: ../test/images

nc: 4
names: ['player', 'ball', 'referee', 'goalkeeper']
```

Split folder train menjadi train dan valid dengan menjalankan split_train_valid_yolo_format_dataset.py (Ratio original 90:10)