from big_sleep import Imagine
from PIL import Image, ImageOps
import os
import random

def generate_images(iterations, prompt):
    dream = Imagine(
        text = prompt,
        text_min = "",
        seed = None,
        larger_clip = False,
        image_size = 512,
        iterations = iterations,
        epochs = 1,
        save_every = 1,
        open_folder = False,
        save_progress = True,
    )

    dream()

def generate_final(seconds, prompt = "psychidelic rainbow fire", framerate = 30):
    iterations = seconds * framerate
    filename = prompt.replace(" ", "_").replace("|", "--")

    print("\n\n\nPHASE 1: Image generation")

    os.chdir("results")
    if "acid_evolve" not in os.listdir("."):
        print("Making acid_evolve directory")
        os.mkdir("acid_evolve")
    os.chdir("acid_evolve")
    
    generate_images(iterations, prompt)

    print("\n\n\nPHASE 2: Image stitching to video")

    os.chdir("..")
    os.system(f"ffmpeg -framerate {framerate} -i acid_evolve/{filename}.%d.png output.mp4")
    
    print("DONE!")

if __name__ == "__main__":
    generate_final(10, "psychidelic rainbow fire", 30)