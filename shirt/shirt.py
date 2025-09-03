import sys
import os
# Pillow package
from PIL import Image, ImageOps

def main():
    # Check command-line arguments
    if len(sys.argv) != 3:
        sys.exit("Usage: python shirt.py input_image output_image")

    input_path = sys.argv[1]
    output_path = sys.argv[2]

    # check file extensions
    valid_extensions = {".jpg", ".jpeg", ".png"}

    # extracts the file extension from the input file path
    input_ext = os.path.splitext(input_path)[1].lower()
    # same but with the output file
    output_ext = os.path.splitext(output_path)[1].lower()

    # check if both images have the same extension
    if (input_ext not in valid_extensions) or (output_ext not in valid_extensions):
        sys.exit("Input and output must be .jpg, .jpeg, or .png files")

    if (input_ext != output_ext):
        sys.exit("Input and output must have the same extension")

    # check if input file exists
    if not (os.path.exists(input_path)):
        sys.exit(f"Input file {input_path} does not exist")

    try:
        # open input image
        with Image.open(input_path) as input_image:
            # open shirt image
            shirt = Image.open("shirt.png")

            # resize and crop input image to match shirt size
            input_image = ImageOps.fit(input_image, shirt.size)

            # overlay shirt on input image
            input_image.paste(shirt, shirt)

            # save the result
            input_image.save(output_path)

    # catch-all exception handler
    except Exception as e:
        # terminate the program immediately
        #  f-string that includes the error message (e) in the output
        sys.exit(f"An error occurred: {e}")

# ensures certain code only runs when the script is executed directly
if __name__ == "__main__":
    main()


