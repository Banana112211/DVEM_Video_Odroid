import cv2

def showWebcam(Input_Channel):
    """"The funciton opens a window and display the webcam Input_Channel"""
    cam = cv2.VideoCapture(Input_Channel)
    while True:
        ret_val, img = cam.read()
        cv2.imshow('my webcam', img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break  # esc to quit
            cv2.destroyAllWindows()

if __name__ == '__main__':
	showWebcam(0)