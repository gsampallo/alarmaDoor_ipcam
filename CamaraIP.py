import cv2

class CamaraIP(object):

    def __init__(self,url):
    	self.url = url

    def capturar(self,archivo):
        cap = cv2.VideoCapture(self.url)
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        frame1 = cv2.resize(gray, (0,0), fx=0.4, fy=0.4) 

        cv2.imwrite(archivo,frame1)
        cap.release()