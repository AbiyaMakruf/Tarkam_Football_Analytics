import cv2

def calculate_time_for_images(start_time, fps_video, fps_capture, num_images):
    # Menghitung durasi antara setiap gambar (dalam detik)
    duration_per_image = fps_capture / fps_video  # Durasi per gambar dalam detik
    
    # Waktu mulai dalam detik
    start_seconds = (start_time // 60) * 60 + (start_time % 60)
    
    # Menghitung waktu selesai setelah mengambil 'num_images' gambar
    end_seconds = start_seconds + (duration_per_image * (num_images - 1))
    
    # Total durasi dalam detik
    total_duration = duration_per_image * (num_images - 1)
    
    # Menghitung menit dan detik dari waktu mulai dan selesai
    start_minutes = start_seconds // 60
    start_seconds = start_seconds % 60

    end_minutes = end_seconds // 60
    end_seconds = end_seconds % 60
    
    print(f"Waktu mulai: {int(start_minutes)}:{int(start_seconds)}")
    print(f"Waktu selesai: {int(end_minutes)}:{int(end_seconds)}")
    print(f"Total durasi: {int(total_duration)} detik")

# Tentukan waktu mulai (16 menit 58 detik)
start_time = (16 * 60) + 58  # dalam detik

# Frame rate video asli (30fps)
fps_video = 30

# Frame rate pengambilan gambar (5fps)
fps_capture = 5

# Jumlah gambar yang diambil
num_images = 25

# Hitung waktu mulai dan selesai untuk 25 gambar pertama
calculate_time_for_images(start_time, fps_video, fps_capture, num_images)
