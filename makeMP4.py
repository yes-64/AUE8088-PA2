import cv2
import os

def images_to_video(image_folder, output_video, fps=25, size=None, is_color=True, format="mp4v"):
    images = [img for img in os.listdir(image_folder) if img.endswith(".jpg")]
    images.sort() 

    if size is None:
        first_image_path = os.path.join(image_folder, images[0])
        first_image = cv2.imread(first_image_path)
        height, width, layers = first_image.shape
        size = (width, height)

    fourcc = cv2.VideoWriter_fourcc(*format)
    video = cv2.VideoWriter(output_video, fourcc, fps, size, is_color)

    for image in images:
        image_path = os.path.join(image_folder, image)
        img = cv2.imread(image_path)
        if img is None: continue
        if size is not None and (img.shape[1], img.shape[0]) != size:
            img = cv2.resize(img, size)
        video.write(img)

    video.release()
    print(f"Video saved at {output_video}")

image_folder = './runs/detect/exp2'
output_video = 'output_video.mp4'

images_to_video(image_folder, output_video, fps=20)
