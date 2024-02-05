import os
import json
import sys

# Get the current script's directory
current_path = os.path.dirname(os.path.abspath(__file__))

# Add the project directory to the system path
project_path = os.path.abspath(os.path.join(current_path, ".."))
sys.path.append(project_path)

from utility.annotation import num_images, image_size,mean_size
from utility.plot import plot_image_width

# current_path = os.path.join(os.path.dirname(__file__))
annotation_folder = os.path.join(current_path, "..", "..", "annotations_trainval2017", "annotations")
json_file_path = os.path.join(annotation_folder, "captions_val2017.json")
try:
    with open(json_file_path, "r") as file:
       file_data = json.load(file)
except FileNotFoundError:
    print(f"Error: File not found - {json_file_path}")    
except json.JSONDecodeError:
    print(f"Error: JSON decoding failed for file - {json_file_path}")    

num_images_result = num_images(file_data)
print(f"Number of images: {num_images_result}")
print("-----------------------------------")

largest_image,smallest_image=image_size(file_data)
print("largest size image is ")
for key,value in largest_image.items():
    print(f"{key}:{value}")
print("----------------------------------------------------")
print("smallest size image is")    
for key, value in smallest_image.items():
    print(f"{key}:{value}")
    
print("----------------------------------------------------")
print("mean size image")
mean_size_image=mean_size(file_data)
for key,value in mean_size_image.items():
    print(f"{key}:{value}")

plot_image_width(file_data)   
    
