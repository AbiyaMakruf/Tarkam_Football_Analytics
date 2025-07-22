import cv2
import os
from tqdm import tqdm  # Import tqdm untuk progress bar

def convert_video_to_images(video_path, output_folder, fps, start_time, end_time):
    # Membaca video
    video_capture = cv2.VideoCapture(video_path)
    video_fps = video_capture.get(cv2.CAP_PROP_FPS)
    total_frames = int(video_capture.get(cv2.CAP_PROP_FRAME_COUNT))

    # Menghitung frame yang sesuai dengan start_time dan end_time
    start_frame = int(start_time * video_fps)  # Menghitung frame start berdasarkan detik
    end_frame = int(end_time * video_fps)      # Menghitung frame end berdasarkan detik

    # Membuat folder output jika belum ada
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Set frame video ke start_frame
    video_capture.set(cv2.CAP_PROP_POS_FRAMES, start_frame)

    # Mengambil gambar berdasarkan frame rate yang diinginkan
    frame_interval = int(video_fps / fps)

    count = 0
    frame_num = start_frame
    total_process_frames = (end_frame - start_frame) // frame_interval  # Total frame yang akan diproses

    # Inisialisasi progress bar
    with tqdm(total=total_process_frames, desc="Proses konversi", unit="frame") as pbar:
        while frame_num < end_frame:
            ret, frame = video_capture.read()
            if not ret:
                break

            if frame_num % frame_interval == 0:
                image_filename = os.path.join(output_folder, f"frame_{count:04d}.jpg")
                cv2.imwrite(image_filename, frame)
                count += 1

            frame_num += 1
            pbar.update(1)  # Update progress bar setiap frame yang diproses

    # Menutup video capture
    video_capture.release()

# Path ke video
video_path = "dataset_video/VEO - IATL IAMA.mp4"
output_folder_5fps = "dataset_image/VEO - IATL IAMA"

# Tentukan waktu mulai dan selesai dalam detik
start_time = (7 * 60) + 26  # 7 menit 26 detik
end_time = start_time + (1 * 60)  # 1 menit dari start_time
# end_time = (109 * 60) + 30   # 101 menit 25 detik

# Mengonversi video menjadi gambar dengan 5fps dalam rentang waktu yang ditentukan
convert_video_to_images(video_path, output_folder_5fps, 5, start_time, end_time)

print("Proses konversi selesai!")
