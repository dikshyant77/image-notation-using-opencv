import cv2 
import matplotlib.pyplot as plt

img = cv2.imread("Unknown.jpeg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

h,w,_ = img.shape

r1_w, r1_h = 30,30
r1_x, r1_y = 80,80
cv2.rectangle(img, (r1_x, r1_y),
              (r1_x+r1_w, r1_y+r1_h),
                (0,255, 255), 3)

r2_w , r2_h = 50,50
r2_x , r2_y =  20, 20
cv2.rectangle(img, (r2_x, r2_y), 
              (r1_x+r1_w, r1_y+r1_h),
                (0,255,255), 3)

c1 = (r1_x + r1_w//2, r1_y + r1_h//2)
c2 = (r2_x + r2_w//2, r2_y + r2_h//2)

cv2.circle(img, c1, 15,(0,255,0), -1)
cv2.circle(img, c2, 15,(0,0,255), -1)

cv2.line(img, c1,c2,(0,255,0), 3)

arrow_x = w - 50
start = (arrow_x, 20)
end = (arrow_x, h-20)

cv2.arrowedLine(img, start, end, (255,255,0), 3)
cv2.arrowedLine(img, end, start, (255,255,0), 3)

cv2.putText(img, f"Height: {h}px",
            (arrow_x - 150 , h//2),
             cv2.FONT_HERSHEY_SIMPLEX, 0.8,
             (255,255,0),2)

cv2.putText(img,"Region_1",(r1_x, r1_y -10),
            cv2.FONT_HERSHEY_SIMPLEX, 0.7,
            (0,255,255), 2)

cv2.putText(img,"Region_2",(r2_x, r2_y -10),
            cv2.FONT_HERSHEY_SIMPLEX, 0.7,
            (255,0,255), 2)

plt.figure(figsize=(10,8))
plt.imshow(img)
plt.axis("off")
plt.show()