import os
import shutil
import random

yolo_img_dir = "images"
yolo_label_dir = "yolo/labels"

target_dataset_dir = "coco"

os.makedirs(f"{target_dataset_dir}/images/train", exist_ok=True)
os.makedirs(f"{target_dataset_dir}/images/val", exist_ok=True)
os.makedirs(f"{target_dataset_dir}/labels/train", exist_ok=True)
os.makedirs(f"{target_dataset_dir}/labels/val", exist_ok=True)

data_list = os.listdir(yolo_label_dir)
for data in data_list:
    data_name = data.split(".")[0]

    if random.uniform(0, 1) > 0.2:
        shutil.copyfile(f"{yolo_img_dir}/{data_name}.png", f"{target_dataset_dir}/images/train/{data_name}.png")
        shutil.copyfile(f"{yolo_label_dir}/{data_name}.txt", f"{target_dataset_dir}/labels/train/{data_name}.txt")

    else:
        shutil.copyfile(f"{yolo_img_dir}/{data_name}.png", f"{target_dataset_dir}/images/val/{data_name}.png")
        shutil.copyfile(f"{yolo_label_dir}/{data_name}.txt", f"{target_dataset_dir}/labels/val/{data_name}.txt")