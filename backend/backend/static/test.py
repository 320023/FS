import cv2
import numpy as np
from pathlib import Path

img_path = Path(r"C:\Users\shuns\flutterstudy\app\backend\static\m4.jpg")

img = cv2.imread(str(img_path))
# cv2.imshow('m4', img)
mask = np.zeros_like(img)


# cv2.waitKey()

hog = cv2.HOGDescriptor()
 
# サポートベクタマシンによる人検出
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
hogParams = {'winStride': (8, 8), 'padding': (32, 32), 'scale': 1.2}
 
# 人を検出した座標
human, r = hog.detectMultiScale(img, **hogParams)
 
# バウンディングボックス
for (x, y, w, h) in human:
    # cv2.rectangle(img, (x, y),(x+w, y+h),(0,50,255), 3)
    img1 = img[y: y + h, x: x + w]
# 画像を表示 
# cv2.imshow("a", img1)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
     
# 検出した画像を保存
print('out_default_'+img_path.stem)
cv2.imwrite(r'C:\Users\shuns\flutterstudy\app\backend\static\out_default_'+img_path.stem+".jpg", img1)
# cv2.destroyAllWindows()