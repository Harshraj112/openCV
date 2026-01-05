import cv2

def get_hand_contour(mask):
    contours, _ = cv2.findContours(
        mask,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    if contours:
        return max(contours, key=cv2.contourArea)
    return None
