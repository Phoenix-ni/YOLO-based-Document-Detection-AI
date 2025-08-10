import os
import shutil
import random

def split_files(image_source_folder, label_source_folder, train_image_folder, val_image_folder, train_label_folder, val_label_folder):
    for folder in [train_image_folder, val_image_folder, train_label_folder, val_label_folder]:
        if not os.path.exists(folder):
            os.makedirs(folder)
    
    all_image_files = [f for f in os.listdir(image_source_folder) if os.path.isfile(os.path.join(image_source_folder, f))]
    random.shuffle(all_image_files)
    
    num_files = len(all_image_files)
    num_train = int(num_files * 0.8)

    for file_name in all_image_files[:num_train]:
        image_source_path = os.path.join(image_source_folder, file_name)
        image_destination_path = os.path.join(train_image_folder, file_name)
        shutil.move(image_source_path, image_destination_path)
        print(f"Moved image {file_name} to {train_image_folder}")
        label_file_name = os.path.splitext(file_name)[0] + '.txt'
        label_source_path = os.path.join(label_source_folder, label_file_name)
        label_destination_path = os.path.join(train_label_folder, label_file_name)
        if os.path.exists(label_source_path):
            shutil.move(label_source_path, label_destination_path)
            print(f"Moved label {label_file_name} to {train_label_folder}")
        else:
            print(f"Label file {label_file_name} not found for image {file_name}")

    for file_name in all_image_files[num_train:]:
        image_source_path = os.path.join(image_source_folder, file_name)
        image_destination_path = os.path.join(val_image_folder, file_name)
        shutil.move(image_source_path, image_destination_path)
        print(f"Moved image {file_name} to {val_image_folder}")
        label_file_name = os.path.splitext(file_name)[0] + '.txt'
        label_source_path = os.path.join(label_source_folder, label_file_name)
        label_destination_path = os.path.join(val_label_folder, label_file_name)
        if os.path.exists(label_source_path):
            shutil.move(label_source_path, label_destination_path)
            print(f"Moved label {label_file_name} to {val_label_folder}")
        else:
            print(f"Label file {label_file_name} not found for image {file_name}")

image_source_folder = 'dataset/437/images'
label_source_folder = 'dataset/437/labels'
train_image_folder = 'train/images'
val_image_folder = 'val/images'
train_label_folder = 'train/labels'
val_label_folder = 'val/labels'
split_files(image_source_folder, label_source_folder, train_image_folder, val_image_folder, train_label_folder, val_label_folder)