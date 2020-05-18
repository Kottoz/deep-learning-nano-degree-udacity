import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    # do what you want with frame
    #  and then save to file
    cv2.imwrite('Desktop/image.png', frame)
    if cv2.waitKey(30) & 0xFF == ord('q'): # you can increase delay to 2 seconds here
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
human = face_detector('Desktop/image.png')
print(if human ? True:False)

def face_detector(img_path):
    img = cv2.imread(img_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray)
    return len(faces) > 0