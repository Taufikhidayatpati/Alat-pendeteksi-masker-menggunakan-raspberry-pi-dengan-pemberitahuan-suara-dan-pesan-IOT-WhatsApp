import numpy as np
import cv2

from utils import CFEVideoConf, image_resize

#Memulai video stream
cap = cv2.VideoCapture(0)

img_path = '/home/pi/STTPHMTE.png'
logo = cv2.imread(img_path, -1)
watermark = image_resize(logo, height=100)
watermark = cv2.cvtColor(watermark, cv2.COLOR_BGR2BGRA)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read() #Memulai video stream
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)
    frame_h, frame_w, frame_c = frame.shape

    # overlay with 4 channels BGR and Alpha
    overlay = np.zeros((frame_h, frame_w, 4), dtype='uint8')
    watermark_h, watermark_w, watermark_c = watermark.shape
    for i in range(0, watermark_h):
        for j in range(0, watermark_w):
            if watermark[i,j][3] != 0:
                offset = 10
                overlay[ i, j] = watermark[i,j]

    cv2.addWeighted(overlay, 0.75, frame, 1.0, 0, frame)

    frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)
    # Display the resulting frame
    cv2.imshow('frame',frame)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
out.release()
cv2.destroyAllWindows()
