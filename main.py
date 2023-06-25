import time
import os
from PIL import Image, ImageFilter
from multiprocessing import Pool, cpu_count
from tabulate import tabulate

# Function to apply blur filter on image
def apply_blur_filter(image_path):
    image = Image.open(image_path)
    # for i in range(3):
    blurred_image = image.filter(ImageFilter.BLUR)
    blurred_image.save(f"blurred_{os.path.basename(image_path)}")

if __name__ == '__main__':
    # images
    image_directory = "images/"

    # paths to images
    image_paths = [os.path.join(image_directory, image_file) for image_file in os.listdir(image_directory)]

    # Single-thread calculations for a single image
    single_image_path = image_paths[0]

    start_time = time.time()
    apply_blur_filter(single_image_path)
    end_time = time.time()
    single_thread_single_image_time = end_time - start_time

    # Multi-thread calculations for a single image
    thread_counts = range(1, cpu_count() + 1)
    single_image_execution_times = []

    for thread_count in thread_counts:
        start_time = time.time()
        with Pool(thread_count) as pool:
            pool.map(apply_blur_filter, [single_image_path])
        end_time = time.time()
        execution_time = end_time - start_time
        single_image_execution_times.append(execution_time)

    # Single-thread calculations for three images
    three_image_paths = image_paths[:3]

    start_time = time.time()
    for image_path in three_image_paths:
        apply_blur_filter(image_path)
    end_time = time.time()
    single_thread_three_images_time = end_time - start_time

    # Multi-thread calculations for three images
    three_image_execution_times = []

    for thread_count in thread_counts:
        start_time = time.time()
        with Pool(thread_count) as pool:
            pool.map(apply_blur_filter, three_image_paths)
        end_time = time.time()
        execution_time = end_time - start_time
        three_image_execution_times.append(execution_time)

    # Single-thread calculations for all images
    start_time = time.time()
    for image_path in image_paths:
        apply_blur_filter(image_path)
    end_time = time.time()
    single_thread_all_images_time = end_time - start_time

    # Multi-thread calculations for all images
    all_images_execution_times = []

    for thread_count in thread_counts:
        start_time = time.time()
        with Pool(thread_count) as pool:
            pool.map(apply_blur_filter, image_paths)
        end_time = time.time()
        execution_time = end_time - start_time
        all_images_execution_times.append(execution_time)

    # Results
    print("Execution time comparison:")
    print("---------------------------")

    headers = ["Threads", "Single Image", "Three Images", "All Images"]
    data = []

    for i, thread_count in enumerate(thread_counts):
        row = [
            thread_count,
            single_image_execution_times[i],
            three_image_execution_times[i],
            all_images_execution_times[i]
        ]
        data.append(row)

    print(tabulate(data, headers=headers, floatfmt=".4f"))
