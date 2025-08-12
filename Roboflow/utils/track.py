from collections import defaultdict
from ultralytics import YOLO
from datetime import datetime
import cv2
import numpy as np

model = YOLO('Z:\RAHMAT SYARIF AZHARI\Project ala ala\Tarkam.id/results\mixed\player_and_ball_class\player_and_ball_class/training/medium\weights/best.pt')

#============================================================================================================================
# results = model.track("Z:\RAHMAT SYARIF AZHARI\Project ala ala\Tarkam.id (MobileApps Advan)/video_source/view_dynamic1_cut1.mp4",
#                       show=True, save=True, tracker="./botsort.yaml")
#============================================================================================================================

input_path = 'Z:\RAHMAT SYARIF AZHARI\Project ala ala\Tarkam.id/video_test/view_dynamic1_cut1.mp4' # Ganti jika lokasi file berbeda
output_path = 'Z:\RAHMAT SYARIF AZHARI\Project ala ala\Tarkam.id/video_result\mixed/v2.1/medium/view_dynamic1_cut1_track.mp4' # Output yang akan disimpan

# Video writer preparation
cap = cv2.VideoCapture(input_path)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(5))
fourcc = cv2.VideoWriter_fourcc(*'mp4v')

out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

time_execution = datetime.now()
frame_id = 0

track_history = defaultdict(lambda: [])

while cap.isOpened():
    before = datetime.now()

    ret, frame = cap.read()
    if not ret:
        break
    if ret:
        results = model.track(frame, persist=True, conf=0.25, iou=0.25, tracker='botsort.yaml')
        boxes = results[0].boxes.xyxy.cpu()
        track_ids = results[0].boxes.id.int().cpu().tolist()
        labels = results[0].boxes.cls

        for box, track_id, label in zip(boxes, track_ids, labels):
            x, y, w, h = box
            track = track_history[track_id]
            track.append((float(x), float(y)))

            x = int(x)
            y = int(y)
            w = int(w)
            h = int(h)

            # if label == 0:
            #     cv2.rectangle(frame, (x, y), (w, h), (0, 0, 255), 2)
            #     cv2.putText(frame, f'{track_id}: ball', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)
            # elif label == 1:
            #     cv2.rectangle(frame, (x, y), (w, h), (255, 255, 255), 2)
            #     cv2.putText(frame, f'{track_id}: goalkeeper', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
            # elif label == 2:
            #     cv2.rectangle(frame, (x, y), (w, h), (255, 0, 0), 2)
            #     cv2.putText(frame, f'{track_id}: player', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
            # elif label == 3:
            #     cv2.rectangle(frame, (x, y), (w, h), (0, 255, 0), 2)
            #     cv2.putText(frame, f'{track_id}: referee', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

            if label == 0:
                cv2.rectangle(frame, (x, y), (w, h), (0, 0, 255), 2)
                cv2.putText(frame, f'{track_id}: ball', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
            elif label == 1:
                cv2.rectangle(frame, (x, y), (w, h), (255, 0, 0), 2)
                cv2.putText(frame, f'{track_id}: player', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
            
        cv2.imshow("YOLO11 Tracking", frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

        out.write(frame)

    # count += int(cap.get(5))
    # cap.set(cv2.CAP_PROP_POS_FRAMES, count)
    print(f"resolusi : {frame.shape[1]} x {frame.shape[0]}")
    print("total frame : ", cap.get(7))
    after = datetime.now()
    print('waktu analytics 1 frame : ', (after-before))
    print("frame ke " + str(frame_id))
    print('====================================================================================================')
    frame_id += 1

cap.release()
cv2.destroyAllWindows()
out.release()

time_execution2 = datetime.now()
print("Waktu eksekusi selama: ", time_execution2-time_execution)
print("Selesai! Video hasil disimpan di:", output_path)