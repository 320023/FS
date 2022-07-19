import cv2

img = cv2.imread(r"hito.jpg")
print(img)

#
path = r'C:\\Users\\81908\\Documents\\MD\\FlutterStudy'
#元画像の読み込み
img = cv2.imread("C:\\Users\\81908\\Documents\\MD\\FlutterStudy\\study\\backend\\static\\hito.jpg")

#読み込んだ画像をグレースケールに変換
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#画像を二値化する
R, binary = cv2.threshold(gray,10,255,cv2.THRESH_BINARY)

cv2.imshow('out_picture', binary)
cv2.imwrite(path + "/" + "save_pic.jpg", binary)  
cv2.waitKey(0) 

#輪郭を算出
contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

 
k = 0
for i in range(0, len(contours)):
    #各輪郭の処理：輪郭の面積を計算
    area = cv2.contourArea(contours[i])
    
    #ノイズ等を除去するために面積でフィルタ 
    if area < 1e2 or 1e5 < area:
        continue
    
    #外接矩形
    if len(contours[i]) > 0:
        rect = contours[i]
        x,y,w,h = cv2.boundingRect(rect)
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        k = k + 1
        
        cv2.imwrite(path + "/" + str(k) +".jpg",img[y:y + h, x:x + w])
#処理後の画像を表示
""" cv2.imshow('out_picture', img)
cv2.imwrite(path + "/" + "save_pic.jpg", img)  
cv2.waitKey(0) """
    
#処理終了
cv2.destroyAllWindows()
