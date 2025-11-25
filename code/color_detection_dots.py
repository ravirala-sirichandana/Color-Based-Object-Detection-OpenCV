import cv2
import numpy as np

# Define the blue color range in HSV
blue_lower = np.array([100, 150, 0])
blue_upper = np.array([140, 255, 255])

# Create a canvas to draw on
canvas = None

# Start video capture
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)  # Flip the frame
    if canvas is None:
        canvas = np.zeros_like(frame)

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Create a mask for blue color
    mask = cv2.inRange(hsv, blue_lower, blue_upper)

    # Find contours in the mask
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if contours and cv2.contourArea(max(contours, key=cv2.contourArea)) > 1000:
        c = max(contours, key=cv2.contourArea)
        x, y, w, h = cv2.boundingRect(c)
        center = (x + w//2, y + h//2)
        cv2.circle(canvas, center, 8, (255, 0, 0), -1)

    # Overlay the drawing on the frame
    frame = cv2.add(frame, canvas)

    cv2.imshow("Drawing", frame)
    cv2.imshow("Mask", mask)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break
    elif key == ord('c'):
        canvas = None  # Clear drawing

cap.release()
cv2.destroyAllWindows()
