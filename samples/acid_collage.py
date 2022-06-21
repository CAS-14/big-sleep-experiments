from big_sleep import Imagine
from PIL import Image, ImageOps
import os
import random

# concat_images.py by @njanakiev on GitHub
def concat_images(image_paths, size, shape=None):
    width, height = size
    images = map(Image.open, image_paths)
    images = [ImageOps.fit(image, size, Image.ANTIALIAS) 
              for image in images]
    
    shape = shape if shape else (1, len(images))
    image_size = (width * shape[1], height * shape[0])
    image = Image.new('RGB', image_size)
    
    print("Initialized the stuff")

    for row in range(shape[0]):
        for col in range(shape[1]):
            offset = width * col, height * row
            idx = row * shape[1] + col
            image.paste(images[idx], offset)
            print(f"Pasted image {idx}")
    
    return image

def generate_images(repeat, iterations, prompt):
    for i in range(repeat):
        print(f"\nGenerating image {i + 1} of {repeat}")

        dream = Imagine(
            text = prompt,
            text_min = "",
            seed = None,
            larger_clip = False,
            image_size = 512,
            iterations = iterations,
            epochs = 1,
            save_every = iterations,
            save_date_time = True,
            open_folder = False,
        )

        dream()

def generate_final(dimensions, iterations, prompt = "psychidelic rainbow fire", generate_new = True):
    print("Preparing")
    
    image_count = dimensions ** 2

    if "output" not in os.listdir("."):
        print("Creating output directory")
        os.mkdir("output")
    os.chdir("output")
    if "acid_trip" not in os.listdir("."):
        print("Making acid_trip dir")
        os.mkdir("acid_trip")
    os.chdir("acid_trip")
    if "final" not in os.listdir("."):
        print("Making final dir")
        os.mkdir("final")

    if generate_new:
        print("\n\n\nPHASE 1: Image generation")
        generate_images(image_count, iterations, prompt)
    else:
        print("\n\n\nPHASE 1 skipped")

    print("\n\n\nPHASE 2: Image stitching")

    images = []
    for result in os.listdir("."):
        if result.endswith(".png"):
            print(f"Found valid file {result}")
            images.append(result)

    image = concat_images(images, (512, 512), (dimensions, dimensions))
    print("Received final image, saving")
    os.chdir("final")
    image.save("final.png", "PNG")
    
    print("DONE!")

if __name__ == "__main__":
    generate_final(8, 100, "psychidelic rainbow fire", True)