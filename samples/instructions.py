instructions = """
            Instructions
            -------------

            1. Select what type of image/video you would like to generate
                > Image Generation (simple) - This generates an image with only a few parameters
                > Image Generation (complex) - This gives you access to more options when generating
                > Evolution Video (simple) - This generates a video that shows the prompt slowly develop over time
                > Evolution Video (complex) - This is the same thing but with more options
                > Instructions - This option takes you to this screen
                > Install Requirements - This will run \"python -m pip install -r requirements.txt\" for you
                                            (not necessary if you are using the .EXE)

            2. Set the options for your generation
                Simple Options:
                    > Image/Video prompt - What you would like the AI to generate, describe it!
                        Note: You can use a vertical slash | to delimit multiple options
                        Example: \"fantasy castle|cartoon style|red\"
                    > Number of iterations per epoch - The amount of detail you would like; more detail takes longer
                    > Number of epochs - The number of times to repeat set amount of iterations
                        An epoch is when the AI can view the whole dataset, so a good ratio would be 100 iterations per epoch and 10 epochs
                    > Number of times to generate over again - This will repeat the entire generation with multiple outputs with the same settings
                        Set this to 1 if you just want one generated
                Complex Options:
                    > Words to avoid - These will be excluded and avoided
                        Example: \"blurry|grainy\"
                    > Use larger model - The larger model may be more realistic, but your GPU may run out of VRAM
                    > Image/Video resolution - 512x512, 256x256, or 128x128
                Video Options:
                    > Video framerate: The speed/smoothness of your video, I recommend setting 30

            3. Press enter when prompted, to start the generation
            4. Sit back and relax, make sure your computer stays on during the cycle

            More Notes:
                - You can press CTRL+C during the generation to cancel it. It may temporary files behind though!
                - If you get an error about the temp_frames directory, delete the temp_frames folder and try again
                - If the video won't play, try using a converter or try making it longer with more iterations
                - On my Nvidia RTX 2070 SUPER on Windows 10/11, each iteration took ~0.4 seconds
            
            More features coming soon!
            """

def instruct():
    print(instructions)