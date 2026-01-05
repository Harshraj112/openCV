import cv2
import math

def count_fingers(contour):
    hull = cv2.convexHull(contour, returnPoints=False)

    if hull is None or len(hull) < 3:
        return 0

    defects = cv2.convexityDefects(contour, hull)

    if defects is None:
        return 0

    finger_count = 0

    for i in range(defects.shape[0]):
        s, e, f, d = defects[i][0]

        if d > 10000:
            finger_count += 1

    return finger_count + 1


def classify_gesture(fingers):
    if fingers == 0 or fingers == 1:
        return "FIST ✊"
    elif fingers == 2:
        return "ONE ☝"
    elif fingers == 3:
        return "TWO ✌"
    elif fingers == 4 or fingers == 5:
        return "PALM ✋"
    else:
        return "UNKNOWN"
