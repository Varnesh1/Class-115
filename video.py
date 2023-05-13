import cv2

vid = cv2.VideoCapture('OBS 27.2.1 (64-bit, windows) - Profile_ Untitled - Scenes_ Miecraft 2022-03-04 18-04-06.mp4')            
if vid.isOpened() == False:
    print('unable to read the video')  

height = int(vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(height)                                                



width = int(vid.get(cv2.CAP_PROP_FRAME_WIDTH))
print(width)    


fps = int(vid.get(cv2.CAP_PROP_FPS))
print(fps)   

while(True):
    ret,frame = vid.read()
    cv2.imshow('webcam', frame)
    if cv2.waitKey(1) == 32:
        break

vid.release()



    #a,b,c,v = 1,2,3,w