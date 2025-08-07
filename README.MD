# ⚽️️ Tarkam Football Analytics

**Selamat datang di repositori _Tarkam Football Analytics_!**  
Project ini bertujuan membangun sistem computer vision untuk menganalisis pertandingan sepak bola lokal (_tarkam_ alias antar-kampung), menggunakan deteksi objek dan pelacakan berdasarkan model YOLOv11 🚀

---

## 🧠 Fitur Utama

- Deteksi objek seperti:
  - 👤 Pemain
  - ⚽ Bola
  - 🎯 Wasit
  - 🥅 Penjaga Gawang
- Tracking pemain sepanjang video pertandingan
- Visualisasi heatmap area pergerakan pemain
- Evaluasi mAP, F1-score, dan waktu inference
- Dapat digunakan untuk prediksi real-time

---

## 📦 Dataset

Dataset dikategorikan menjadi:

| Sumber     | Kategori                 | Versi Roboflow | Jumlah Kelas                   |
|------------|--------------------------|----------------|--------------------------------|
| Internal   | All Class                | v4             | Player, Ball, Referee, Goalkeeper |
| Internal   | Player and Ball          | v5             | Player, Ball                   |
| External   | All Class                | v2             | Player, Ball, Referee, Goalkeeper |
| Mixed      | All Class (Merged)       | v1             | Player, Ball, Referee, Goalkeeper |
| Mixed      | Player and Ball (Merged) | v2             | Player, Ball                   |

> 🔗 Dataset diunduh otomatis menggunakan API Roboflow di dalam notebook.

---

## ⚙️ Instalasi

```bash
pip install -U ultralytics
pip install roboflow
```

---

## 🏋️‍♀️ Pelatihan Model

Model yang dilatih:

- `yolo11n.pt` (nano)
- `yolo11s.pt` (small)
- `yolo11m.pt` (medium)

### Contoh konfigurasi pelatihan:

```python
model.train(
  data="path/to/data.yaml",
  epochs=150,
  imgsz=640,
  batch=16,
  project="results/training",
  name="small",
  device=0
)
```

### Evaluasi:

```python
model.val(
  data="path/to/data.yaml",
  imgsz=640,
  project="results/validation",
  name="small",
  split="test"
)
```

---

## 📈 Hasil Pelatihan

| Dataset             | Model     | mAP50 | Waktu Latih | F1-Score |
|---------------------|-----------|-------|-------------|----------|
| Internal All Class  | YOLOv11-n | 0.841 | 21m 13s     | 0.75     |
| Internal All Class  | YOLOv11-s | 0.894 | 29m 50s     | 0.82     |
| Internal All Class  | YOLOv11-m | 0.907 | 47m 12s     | 0.85     |

ℹ️ Selengkapnya: [Ringkasan Hasil](https://docs.google.com/spreadsheets/d/13dVkRmgKa6BuhOga8YFoFF8t7M6MHB0yttlljOvkN-g/edit?usp=sharing)

---

## 🔍 Prediksi Gambar & Video

Contoh penggunaan model:

```python
model = YOLO("path/to/best.pt")
model("path/to/image_or_video.mp4", save=True)
```

---

## 🧭 Pelacakan Video

```python
model.track(
  source="path/to/video.mp4",
  tracker="botsort.yaml",
  save=True
)
```

---

## 🤝 Kontribusi

Pull request dan saran sangat diterima!  
Jangan lupa 🌟 repo ini jika bermanfaat bagi Anda 😄

---
