#!/usr/bin/env python3
import cv2
import numpy as np

cap = cv2.VideoCapture(0) # 1st webcam
if not cap.isOpened():
  raise RuntimeError("No webcam")
ret, frame = cap.read()   # 1st frame
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

N=50                      # ring buffer length (amplitude calculation)
line_x=420                # X-axis position
line_y = gray.shape[0]//2 # middle of image
dy=20                     # correlation line length
print(len(gray[1,:]))
print(len(gray[:,1]))
values=np.zeros(N)
valpos=0

reference_line = gray[line_y:line_y+dy,line_x].astype(np.float32)
reference_line -= np.mean(reference_line)
while True:
  ret, frame = cap.read()
  if not ret:
    break
  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  current_line = gray[line_y:line_y+dy,line_x].astype(np.float32)
  current_line -= np.mean(current_line)
  corr = np.correlate(current_line, reference_line, mode='full')
  peak_idx = np.argmax(corr)
  corr_e = corr[peak_idx-1]
  corr_l = corr[peak_idx+1]
  corr_p = corr[peak_idx]
  fine_corr = 0.5*(corr_e-corr_l)/(corr_e+corr_l-2*corr_p)
  shift = peak_idx - (len(reference_line)-1)+fine_corr
  values[valpos]=shift
  valpos+=1
  valpos=np.mod(valpos,N)
  display = frame.copy()
  cv2.line(display, (line_x, line_y), (line_x, line_y+dy), (0, 255, 0), 2)
  if (shift<0):
    text = f"{shift:.2f} px A={np.std(values-np.mean(values)):.2f}"
  else:
    text = f"+{shift:.2f} px A={np.std(values-np.mean(values)):.2f}"
  cv2.putText(display, text, (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 255), 2)
  print(f"{shift:.2f} {np.std(values-np.mean(values)):.2f}")
  cv2.imshow("correlation", display)
  key = cv2.waitKey(1) & 0xFF
  if key == ord('r'):
    reference_line = current_line.copy()
    print("Reference updated.")
  elif key == ord('q'):
    break
cap.release()
cv2.destroyAllWindows()
