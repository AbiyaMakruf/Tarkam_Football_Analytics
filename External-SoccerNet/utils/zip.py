import shutil
import os

def zip_folder(source_folder, output_zip_path):
    # Pastikan path tidak ada ekstensi .zip karena shutil.make_archive menambahkannya sendiri
    if output_zip_path.endswith('.zip'):
        output_zip_path = output_zip_path[:-4]

    # Pastikan folder sumber ada
    if not os.path.exists(source_folder):
        raise FileNotFoundError(f"Folder tidak ditemukan: {source_folder}")

    # Buat zip
    shutil.make_archive(output_zip_path, 'zip', source_folder)
    print(f"✅ Folder '{source_folder}' berhasil di-zip ke '{output_zip_path}.zip'")

# ===============================
# Contoh penggunaan:
source_folder = 'dataset_yolo_format_split/5000'
output_zip_path = 'dataset_yolo_format_split/5000'  # tanpa .zip
# ===============================

# Pastikan folder tujuan ada
os.makedirs(os.path.dirname(output_zip_path), exist_ok=True)

# Jalankan
zip_folder(source_folder, output_zip_path)
