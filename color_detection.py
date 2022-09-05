import cv2
cap=cv2.VideoCapture(0)
while True:
    _,frame=cap.read()
    height,width,_=frame.shape
    cen_x=int(width/2)
    cen_y=int(height/2)
    pix_center_color=frame[cen_y,cen_x]
    cv2.circle(frame,(cen_x,cen_y),10,(255,0,0),6)
    b, g, r = (pix_center_color[0]), (pix_center_color[1]), (pix_center_color[2])
    rs = (max(r, g, b))
    if rs == r:
        color='red'
    elif rs == g:
        color = 'green'
    else:
        color = 'blue'
    cv2.rectangle(img=frame, pt1=(45, 100), color=(int(b), int(g), int(r)), pt2=(130, 100), thickness=80)
    cv2.putText(frame, (color), (20, 110), cv2.FONT_HERSHEY_PLAIN, 3, (255,255, 255), 5)
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) ==27:
        break
cap.release()
