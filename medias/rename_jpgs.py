import os

def rename_jpgs(directory):
    """
    将指定目录（directory）下的所有 .jpg 文件按字典序重命名为 0.jpg, 1.jpg, 2.jpg, ...
    """
    # 切换到目标目录
    os.chdir(directory)

    # 获取所有以 .jpg 结尾的文件（不区分大小写），并按名称排序
    jpg_files = [f for f in os.listdir('.') if f.lower().endswith('.jpg')]
    jpg_files.sort()

    # 依次重命名
    for idx, old_name in enumerate(jpg_files):
        new_name = f"{idx}.jpg"
        # 如果目标文件名已经存在，先跳过或处理冲突
        # if os.path.exists(new_name):
        #     print(f"跳过重命名：目标文件 {new_name} 已存在，原文件 {old_name} 保持不变。")
        #     continue
        os.rename(old_name, new_name)
        print(f"{old_name} → {new_name}")

if __name__ == "__main__":
    # 将下面的路径替换为你存放 jpg 图片的文件夹
    folder_path = r"C:\code_old\code\blog\themes\hexo-theme-matery\source\medias\featureimages"
    rename_jpgs(folder_path)