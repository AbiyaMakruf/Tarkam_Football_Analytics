import os
import shutil

# Mapping dari gameID ke daftar folder
gameid_mapping = {
    7: ['SNMOT-116', 'SNMOT-117', 'SNMOT-118', 'SNMOT-119', 'SNMOT-120', 'SNMOT-121', 'SNMOT-122', 'SNMOT-123',
        'SNMOT-124', 'SNMOT-125', 'SNMOT-126', 'SNMOT-127', 'SNMOT-128', 'SNMOT-129', 'SNMOT-130', 'SNMOT-131'],
    8: ['SNMOT-132', 'SNMOT-133', 'SNMOT-134', 'SNMOT-135', 'SNMOT-136', 'SNMOT-137', 'SNMOT-138', 'SNMOT-139',
        'SNMOT-140', 'SNMOT-141', 'SNMOT-142', 'SNMOT-143', 'SNMOT-144', 'SNMOT-145', 'SNMOT-146', 'SNMOT-147',
        'SNMOT-148', 'SNMOT-149', 'SNMOT-150'],
    11: ['SNMOT-187', 'SNMOT-188', 'SNMOT-189', 'SNMOT-190', 'SNMOT-191', 'SNMOT-192', 'SNMOT-193', 'SNMOT-194',
         'SNMOT-195', 'SNMOT-196', 'SNMOT-197', 'SNMOT-198', 'SNMOT-199', 'SNMOT-200']
}

# Paths
src_img_dir = 'dataset_yolo_format/test/images'
src_lbl_dir = 'dataset_yolo_format/test/labels'
dst_root = 'dataset_yolo_format_split/test_per_matchid'

# Buat mapping SNMOT folder ke gameID
folder_to_gameid = {}
for gid, folders in gameid_mapping.items():
    for f in folders:
        folder_to_gameid[f] = gid

# Buat direktori tujuan dan copy file
for file_name in os.listdir(src_img_dir):
    if not file_name.endswith('.jpg'):
        continue

    # Ambil prefix SNMOT-xxx
    prefix = file_name.split('_')[0]
    game_id = folder_to_gameid.get(prefix)
    if game_id is None:
        continue  # skip jika tidak ada mapping

    # Buat path tujuan
    match_folder = f"matchid{game_id}"
    dst_img_dir = os.path.join(dst_root, match_folder, 'images')
    dst_lbl_dir = os.path.join(dst_root, match_folder, 'labels')
    os.makedirs(dst_img_dir, exist_ok=True)
    os.makedirs(dst_lbl_dir, exist_ok=True)

    # Copy image
    shutil.copy2(os.path.join(src_img_dir, file_name), os.path.join(dst_img_dir, file_name))

    # Copy label
    label_file = file_name.replace('.jpg', '.txt')
    src_label_path = os.path.join(src_lbl_dir, label_file)
    if os.path.exists(src_label_path):
        shutil.copy2(src_label_path, os.path.join(dst_lbl_dir, label_file))

print("✅ Split per gameID selesai.")
