import time
import os
from PIL import Image, ImageFilter
from multiprocessing import Pool

# Function to apply blur filter on image
def apply_blur_filter(image_path):
    image = Image.open(image_path)
    for i in range(3):
        blurred_image = image.filter(ImageFilter.BLUR)
    blurred_image.save(f"blurred_{os.path.basename(image_path)}")

if __name__ == '__main__':
    # images
    image_directory = "images/"

    # paths to images
    image_paths = [os.path.join(image_directory, image_file) for image_file in os.listdir(image_directory)]

    # Single-thread calculations
    start_time = time.time()
    for image_path in image_paths:
        apply_blur_filter(image_path)
    end_time = time.time()
    single_thread_time = end_time - start_time

    # multiple-threads calculations
    start_time = time.time()
    with Pool() as pool:
        pool.map(apply_blur_filter, image_paths)
    end_time = time.time()
    multi_thread_time = end_time - start_time

    # results
    print(f"Execution time with one thread: {single_thread_time} seconds")
    print(f"Execution time with multiple threads: {multi_thread_time} seconds")
