import os

def rename_images(root_folder):
    # 定义支持的图片文件扩展名
    image_extensions = ('.png', '.jpg', '.jpeg', '.bmp', '.gif')
    image_files = []

    # 遍历指定文件夹及其子文件夹
    for root, dirs, files in os.walk(root_folder):
        for file in files:
            if file.lower().endswith(image_extensions):
                image_files.append(os.path.join(root, file))

    # 按路径排序
    image_files.sort()

    # 重命名图片文件
    for index, old_path in enumerate(image_files, start=0): # 从0开始重命名
        # 构建新的文件名
        new_name = f"{index}.jpg"
        # 获取原文件所在目录
        dir_path = os.path.dirname(old_path)
        new_path = os.path.join(dir_path, new_name)
        try:
            # 重命名文件
            os.rename(old_path, new_path)
            print(f"已将 {old_path} 重命名为 {new_path}")
        except Exception as e:
            print(f"重命名 {old_path} 时出错: {e}")

if __name__ == "__main__":
    # 替换为你要处理的文件夹路径
    target_folder = "/home/zyb/百度飞桨领航团/学习项目/CV项目/第五次汇报/paddle_dataset/table_gen_dataset/img"
    rename_images(target_folder)
