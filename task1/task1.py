"""
 Download the test images from this Kaggle dataset, and place them all in a folder
 Define a function in the jupyter notebook to do the following tasks:


■ Input: Takes the path of the folder as the input

■ Process:
● Loads all the images and convert them to an array
● Convert all the images to grayscale images

■ Output:
● Number of images
● Format type of the images
● Saving all the grayscale images to another folder
Bonus:
Convert the background of the images to white before converting them to
grayscale
"""

import cv2
import os


#function to load all the images and convert them to an array
def load_images_from_folder(folder):
    images = []
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder,filename),cv2.IMREAD_GRAYSCALE)
        if img is not None:
            images.append(img)
            cv2.imwrite(f'results/{folder}/gray_{filename}',img)
    return images

if __name__ == '__main__':
    folderName = input()
    images = load_images_from_folder(folderName)
    print(len(images))