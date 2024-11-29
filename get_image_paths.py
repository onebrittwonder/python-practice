import os

def get_image_paths(folder_path):
    image_extensions = ".svg"
    image_paths = []

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path) and any(filename.endswith(ext) for ext in image_extensions):
            image_paths.append(file_path)

    return image_paths

folder_path = #r"C:\#######\####\####"
image_paths = get_image_paths(folder_path)

print(image_paths)