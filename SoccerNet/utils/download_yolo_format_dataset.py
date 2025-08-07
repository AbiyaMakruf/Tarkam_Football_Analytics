# Codingan Python untuk mengunduh dataset dalam format YOLO dari Google Drive.

import gdown
import zipfile
import os

# ID file Google Drive (bukan URL penuh)
file_id = '1SosFwKwczp4Ie1rZ3kNICOka5N-o-1BC'
output_zip = 'downloaded_file.zip'

# Download file ZIP
gdown.download(f'https://drive.google.com/uc?id={file_id}', output_zip, quiet=False)

# # Ekstrak file ZIP
# with zipfile.ZipFile(output_zip, 'r') as zip_ref:
#     zip_ref.extractall('./')

# # (Opsional) Hapus file ZIP setelah extract
# os.remove(output_zip)

print("✅ Download dan ekstrak selesai.")