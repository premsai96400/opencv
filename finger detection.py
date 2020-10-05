import cv2
import numpy as np 
Window = 'interest'    
def main():
    sak = np.zeros((512,512,3),np.uint8)
    cap = cv2.VideoCapture(0)
    if cap.isOpened():
         ret,frame = cap.read()
    else:
         ret = False


    while ret:
    
        ret, frame = cap.read()
        cv2.rectangle(frame,(50,50),(450,450),(255,0,0),1)
        a = frame[50:450,50:450]
        b = cv2.cvtColor(a,cv2.COLOR_BGR2GRAY)
        c = cv2.blur(b,(3,3))
        ret,d = cv2.threshold(c, 100, 255, cv2.THRESH_BINARY_INV) 
        space = []
        kiran = []
        def number(event,x,y,flags,param):
            if event == cv2.EVENT_LBUTTONDOWN:
                contours,hierarchy = cv2.findContours(d,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
                cv2.circle(slak,(x,y),50,(255,0,0),-1)
                space = contours.copy() 
                print('KIRAN')
            elif event == cv2.EVENT_RBUTTONDOWN:
                contours,hierarchy = cv2.findContours(d,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
                kiran = contours.copy()
                print('kir')
        cv2.setMouseCallback(Window,number)
        fingers = list(set(space)-set(kiran))
 #       contours,hierarchy = cv2.findContours(d,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        for i in range(len(fingers)):
            hull = cv2.convexHull(fingers[i])
            cv2.drawContours(d, [hull], -1, (255, 0, 0), 2)
        cv2.imshow('preview',frame)
        cv2.imshow(Window ,slak)
 #       print(fingers,'SAI')
        if cv2.waitKey(1) == 27: 
            break

    cv2.destroyAllWindows()
    cap.release()
    
if _name_ == "_main_":
    main()
