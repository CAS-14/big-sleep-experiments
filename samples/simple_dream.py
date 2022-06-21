from big_sleep import Imagine
from os import chdir

"""
NOTE
text : the text you want to generate
text_min : the text you want to avoid
seed : set to None for a random seed, or use a number
larger_clip : set to True to use larger model
image_size: 64, 128, or 512
iterations : amount of iterations per epoch
epochs : amount of times to do iterations and check image after
save_every : how often (iterations) to re-save the image
save_progress : save new versions every save instead of rewriting
save_date_time : whether to name file with date and time
append_seed : whether to name file with seed
open_folder : whether to open the file explorer window

NOTE
0.4 secs per iteration -> MINS*60/0.4 = total iterations goal
- for 10 min generation, use 500 iterations and 3 epochs
- for a 1 min epoch, use 150 generations
Good setting is 200 iters, 5 epochs, SE 100
"""

def generate(text, iterations = 100, epochs = 1, save_every = 50, text_min = ""):
    print(f"Generating \"{text}\" with {epochs} epochs of {iterations} iterations each, saving every {save_every}")
    print(f"Expected to take {iterations * epochs * 0.4 / 60} minutes")

    dream = Imagine(
        text = text,
        text_min = text_min,
        seed = None,
        larger_clip = False,
        image_size = 64,
        iterations = iterations,
        epochs = epochs,
        save_every = save_every,
        save_progress = False,
        save_date_time = False,
        append_seed = False,
        open_folder = False,
    )

    dream()

def repeat(times, prompt):
    
    for i in range(times):
        print(f"STARTING GENERATION {i + 1}")
        generate(prompt)
        print(f"GENERATION {i + 1} COMPLETE")

    print("ALL GENERATIONS COMPLETE")

if __name__ == "__main__":
    chdir("output")
    generate("green colors", 20, 1, 20)