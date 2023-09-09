# create blank masks whitch is needed for training
import cv2
import numpy as np
import os

height = 512
width = 512
project_dir = "./woman_dance"
process_name = "woman"

train_dir = f"{project_dir}/{process_name}_train"
train_input_filtered_dir = f"{train_dir}/input_filtered"
train_mask_dir = f"{train_dir}/mask"
train_output_dir = f"{train_dir}/output"

gen_dir = f"{project_dir}/{process_name}_gen"
gen_input_filtered_dir = f"{gen_dir}/input_filtered"
gen_mask_dir = f"{gen_dir}/mask"
gen_output_dir = f"{gen_dir}/output"

os.makedirs(train_mask_dir, exist_ok=True)
os.makedirs(gen_mask_dir, exist_ok=True)

blank = np.zeros((height, width, 3))
blank += 255 # white

train_input_filtered_list = os.listdir(train_input_filtered_dir)
for img in train_input_filtered_list:
  mask_img_path = f"{train_mask_dir}/{img}"
  print(mask_img_path)
  cv2.imwrite(mask_img_path, blank)

gen_input_filtered_list = os.listdir(gen_input_filtered_dir)
for img in gen_input_filtered_list:
  mask_img_path = f"{gen_mask_dir}/{img}"
  print(mask_img_path)
  cv2.imwrite(mask_img_path, blank)