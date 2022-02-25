"""
1. Download the data from the link here
2. Write a function in python script to do the following:
i. Inputs: Input the folder name and csv filename through command line
ii. To-Do:
1. Read all the images
2. Read the csv file, and get the image label names and coordinates
3. Draw the bounding boxes for every image, using the
corresponding image’s coordinates (Use different colour and
thickness for the bounding boxes)
4. Add labels for every image (Use different font, font colour, font
size)
5. Create another folder and save all the images to the folder
6. Push the code to GitHub, and show few samples of the before and after on the Readme.md file.
"""

import os
import cv2

# Function to read the csv file and get the image label names and coordinates
def read_csv(csv_file:str) -> dict:
    """
    Function to read the csv file and get the image label names and coordinates
    :param csv_file: csv file
    :return: image_info
    """
    image_info = {}
    with open(csv_file, 'r') as f:
        for line in f:
            line = line.strip().split(',')
            image_info[line[0]] = line[1:]
    return image_info

#function to draw the bounding boxes for every image in a given folder
def draw_bounding_box(image_folder:str, image_info:dict) -> None:
    """
    Function to draw the bounding boxes for every image in a given folder
    :param image_path: image path
    :param image_info: image info
    :return: None
    """
    for image_path in os.listdir(image_folder):
        image = cv2.imread(os.path.join(image_folder,image_path),cv2.IMREAD_UNCHANGED)
        coordinates = image_info.get(image_path)
        x1,y1,x2,y2 = tuple(map(int, coordinates[3:]))
        label = coordinates[0]
        cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(image, label, (x1, y1), cv2.QT_FONT_NORMAL, 1, (0, 0, 0), 1)
        cv2.imwrite(f'results/cat/bounded_{image_path}',image)

if __name__ == '__main__':
    image_folder, csv_file = input().strip().split()
    image_info = read_csv(csv_file)
    draw_bounding_box(image_folder, image_info)