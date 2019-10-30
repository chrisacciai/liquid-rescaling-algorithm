import sys
import time
from seam_carving import SeamCarving
from PIL import Image

fp = Image.open("test1.png")
pixels = fp.load()
w, h = fp.size
image_data = [[[0 for k in range(3)] for j in range(w)] for i in range(h)]
for i in range(w):
    for j in range(h):
        image_data[j][i][0] = pixels[i, j][0]
        image_data[j][i][1] = pixels[i, j][1]
        image_data[j][i][2] = pixels[i, j][2]


# Call the closest_pair function passing in the
# contents of the file
start = time.time()
sc = SeamCarving()
weight = sc.run(image_data)
print("weight: " + str(weight))
print("seam: " + str(sc.getSeam()))
end = time.time()
print("time: "+ str(end-start))

#Uncomment to display seam on image 
seam = sc.getSeam() 
y = 0
for x in seam:
    fp.putpixel((x,y), 0x000000ff)
    y = y+1
fp.show()


