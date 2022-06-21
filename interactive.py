from tempfile import TemporaryFile
from big_sleep import Imagine
from pick import pick
import os
import shutil
import samples.instructions as instructions

def main():
    print("Loading...")
    try:
        os.mkdir("output")
    except:
        pass

    action_name, action = pick(["Image Generation (simple)", "Image Generation (complex)", "Evolution Video (simple)", "Evolution Video (complex)", "Instructions", "Install Requirements"], "Welcome to InterSleep! Please select what you would like to generate:", ">")
    print(f"\n\nYou have selected {action_name}")

    if 0 <= action <= 3:

        complexgen = False if action in [0, 2] else True
        progression = True if 1 < action < 4 else False

        media = "video" if progression else "image"

        print("Please input your options below.\n")

        text = input(f"{media.capitalize()} prompt: ")
        text_min = input("Words to avoid: ") if complexgen else ""
        
        larger_clip = pick([False, True], "Use larger model:", ">")[0] if complexgen else False
        print(f"Use larger model: {larger_clip}") if complexgen else None

        image_size = pick([512, 256, 128], f"{media.capitalize()} resolution:", ">")[0] if complexgen else 512
        print(f"{media.capitalize()} resolution: {image_size}x{image_size}") if complexgen else None

        iterations = int(input("Number of iterations per epoch: ")) 
        epochs = int(input("Number of epochs: "))
        
        if not progression:
            save_every = int(input("Save every: ")) if complexgen else iterations

            save_progress = pick([False, True], "Save progress as separate images:", ">")[0] if complexgen else False
            print(f"Save progress: {save_progress}") if complexgen else None
        
        else:
            save_every = 1
            save_progress = True

        repeat = int(input("Number of times to generate over again: "))

        filename = text.replace(" ", "_").replace("|", "--")
        if text_min != "":
            filename += "_wout_" + text_min.replace(" ", "_").replace("|", "--")

        if progression:
            framerate = input("Video framerate: ")

        cancel = input("\nPress enter now to begin generating! (or type \"cancel\" to cancel)").lower()

        if cancel == "cancel":
            print("Cancelled.")
            return

        for i in range(repeat):
            print("Initializing image dream process...")

            dream = Imagine(
                text = text,
                text_min = text_min,
                seed = None,
                larger_clip = larger_clip,
                image_size = image_size,
                iterations = iterations,
                epochs = epochs,
                save_every = save_every,
                save_progress = save_progress,
                open_folder = False,
            )

            prefix = f"[{i + 1}/{repeat}]" if repeat > 1 else ""
            file_suffix = f"_{i + 1}" if repeat > 1 else ""

            if progression:
                if "temp_frames" not in os.listdir("."):
                    os.mkdir("temp_frames")

                print(f"{prefix} Starting Phase 1: Image generation")

            os.chdir("temp_frames" if progression else "output")

            print("Starting generation!\n")

            try:
                dream()

            except KeyboardInterrupt:
                print("Cancelled by keyboard interrupt! Cleaning up and exiting...")
                
                shutil.rmtree("temp_frames") if progression else None
                return

            if not progression:
                os.rename(f"{filename}.png", f"{filename}{file_suffix}.png")

            os.chdir("..")

            print(f"\n\n\n\n{prefix} Image generation complete!")
            
            if progression:
                print(f"{prefix} Starting Phase 2: Image stitching to video")
                os.system(f"ffmpeg -framerate {framerate} -i temp_frames/{filename}.%d.png -pix_fmt yuv420p -c:v libx264 -crf 0 -r 30 output/{filename}{file_suffix}.mp4")
                print(f"\n\n{prefix} Video generation complete! Cleaning up...")

                shutil.move(f"temp_frames/{filename}.png", f"output/{filename}{file_suffix}.png")
                shutil.rmtree("temp_frames")

        print(f"All done! Thank you for using InterSleep. Your {media}s are in the \"output\" directory.")

    else:

        if action == 4:
            instructions.instruct()
            input("Scroll up for more instructions. Press enter to return to the main menu.")

            main()

        elif action == 5:
            print("\nInstalling required packages from requirements.txt (command used: \"python -m pip install -r requirements.txt\")")
            os.system("python -m pip install -r requirements.txt")
            input("Attempted to install packages, probably worked!\nPress enter to continue.")

            main()

if __name__ == "__main__":
    main()