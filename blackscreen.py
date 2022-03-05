import cv2
import numpy as np

fourcc = cv2.VideoWriter_fourcc(*'XVID')
output_file = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))
cap = cv2.VideoCapture(0)
frame = 0

for i in range(60):
    ret, frame = cap.read()
frame = np.flip(frame, axis=1)

while (cap.isOpened()):
    ret, img = cap.read()
    if not ret:
        break
    img = np.flip(img, axis=1)

    frame = cv2.resize(frame, (640,480))
    img = cv2.resize(img, (640,480))

    u_black = np.array([104,153,70])
    l_black = np.array([30,30,0])

    mask = cv2.inRange(frame, l_black, u_black)
    res = cv2.bitwise_and(frame, frame, mask = mask)

    f = frame - res
    f = np.where(f == 0, img, f)

    final_output = cv2.addWeighted(res, 1, f, 1, 0)
    output_file.write(final_output)

    cv2.imshow("pic", final_output)
    cv2.waitKey(1)

cap.release()
out.release()
cv2.destroyAllWindows()
