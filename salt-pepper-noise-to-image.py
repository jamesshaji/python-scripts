import numpy as np
import os
import cv2
import random


def sp_noise(image,prob):
    '''
    Add salt and pepper noise to image
    prob: Probability of the noise
    '''
    output = np.zeros(image.shape,np.uint8)
    thres = 1 - prob 
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            #print(image[i][j].size)
            if(image[i][j].size > 3):
                if(not image[i][j][3] == 0):
                    rdn = random.random()
                    if rdn < prob:
                        output[i][j] = 0
                    elif rdn > thres:
                        output[i][j] = 255
                    else:
                        output[i][j] = image[i][j]
            else:
                rdn = random.random()
                if rdn < prob:
                    output[i][j] = 0
                elif rdn > thres:
                    output[i][j] = 255
                else:
                    output[i][j] = image[i][j]
                
    return output

def gaussion_noise(image):
    gauss = np.random.normal(0,1,image.size)
    gauss = gauss.reshape(image.shape[0],image.shape[1],image.shape[2]).astype('uint8')
    img_gauss = cv2.add(image,gauss)
    return img_gauss

path = 'PATH_TO_THE_FOLDER'

files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        if '.png' in file:
            files.append(os.path.join(r, file))

for f in files:
    print(f)
    image = cv2.imread(f,-1)
    noise_img = sp_noise(image,0.05)
    print(f)
    #noise_img = gaussion_noise(image)
    cv2.imwrite(f, noise_img)
