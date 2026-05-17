import cv2
import matplotlib.pyplot as plt
image=cv2.imread('saturn.jpg')
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
height,width,_=image.shape
leftarrow=(20,height-50)
rightarrow=(width-20,height-50)
cv2.arrowedLine(image_rgb,leftarrow,rightarrow,(255,255,0),3,tipLength=0.05)
cv2.arrowedLine(image_rgb,rightarrow,leftarrow,(255,255,0),3,tipLength=0.05)
widthlabel=(width//2-100,height-80)
cv2.putText(image_rgb,f'Width:{width}px',widthlabel,cv2.FONT_HERSHEY_SIMPLEX,0.8,(255,255,0),2)
cv2.imwrite('output_images/annotated_width.jpg', image_rgb)
plt.imshow(cv2.cvtColor(image_rgb, cv2.COLOR_BGR2RGB))
plt.title("Annotated Image with Bi-Directional Width Arrows")
plt.axis('off')
plt.show()