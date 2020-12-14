import cv2
import pandas as pd

tryion_img=cv2.imread("./Filter Photos/Before_filter.jpg")

print(tryion_img.shape)

tryion_img=tryion_img.reshape(-1,3)

print(tryion_img.shape)

df=pd.DataFrame(tryion_img,columns=["Channel 1","Channel 2","Channel 3"])

df.to_csv("tryion_filter.csv",index=False)