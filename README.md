## Multithreading Image Blur Application

This is a simple Python program that demonstrates the benefits of distributing computations across multiple threads using the `multiprocessing` library. The program applies a blur filter to a collection of images and compares the execution time between single-threaded and multithreaded approaches.

### Prerequisites

- Python 3.x
- PIL (Python Imaging Library) package

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/image-blur.git
   ```

2. Navigate to the project directory:

   ```bash
   cd image-blur
   ```

3. Install the required dependencies:

   ```bash
   pip install pillow
   ```

### Usage

1. Place your images in the `images/` directory.

2. Run the program:

   ```bash
   python image_blur.py
   ```

### How It Works

1. The program defines the `apply_blur_filter` function, which opens an image, applies a blur filter, and saves the resulting image with a "blurred_" prefix.

2. It retrieves a list of image paths from the `images/` directory.

3. Single-threaded approach:
   - The program iterates over each image path.
   - It applies the blur filter to each image sequentially and measures the execution time.

4. Multithreaded approach:
   - The program creates a pool of processes using the `multiprocessing.Pool` class.
   - It uses the `map` method to apply the blur filter to the images concurrently.
   - The pool distributes the workload among multiple threads, resulting in faster execution.
   - It measures the execution time.

5. The program outputs the execution time for both approaches, allowing you to observe the time difference between single-threaded and multithreaded execution.

### Results

Running the program demonstrates the benefits of using multithreading for image processing tasks. The multithreaded approach significantly reduces the execution time compared to the single-threaded approach, especially when dealing with a large number of images.

Feel free to modify the program or incorporate it into your own projects as an example of leveraging multithreading for parallel computations.

For more information on the `multiprocessing` module and Python multithreading, refer to the official Python documentation.
