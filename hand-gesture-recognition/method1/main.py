import cv2
from camera import start_camera
from skin_detection import detect_skin
from hand_contour import get_hand_contour
from gesture_logic import count_fingers, classify_gesture
from utils import draw_text

cam = start_camera()

while True:
    ret, frame = cam.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    mask = detect_skin(frame)

    contour = get_hand_contour(mask)
    if contour is not None:
        cv2.drawContours(frame, [contour], -1, (255,0,0), 2)
        fingers = count_fingers(contour)
        gesture = classify_gesture(fingers)
        draw_text(frame, gesture)

    cv2.imshow("Hand Gesture", frame)
    cv2.imshow("Mask", mask)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cam.release()
cv2.destroyAllWindows()
