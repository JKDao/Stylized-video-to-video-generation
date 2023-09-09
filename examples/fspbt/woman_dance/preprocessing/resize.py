from PIL import Image
import os

# Set the directory paths for the original and resized images
original_directory = './tmp'
resized_directory = '../woman_gen/whole_video_input'

# Define the amount to move the center point
move_x = 80

# Loop through all files in the original directory
for filename in os.listdir(original_directory):
    # Skip any non-image files
    if not filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
        continue

    # Open the original image
    original_image = Image.open(os.path.join(original_directory, filename))

    # Get the dimensions of the original image
    original_width, original_height = original_image.size

    # Calculate the center coordinates of the original image
    center_x = original_width / 2 + move_x
    center_y = original_height / 2

    # Calculate the whole_video_input boundaries based on the center coordinates and the desired whole_video_input size
    crop_size = min(original_width, original_height)
    left = center_x - crop_size / 2
    top = center_y - crop_size / 2
    right = center_x + crop_size / 2
    bottom = center_y + crop_size / 2

    # Crop the image
    cropped_image = original_image.crop((left, top, right, bottom))

    # Resize the cropped image to 512x512
    resized_image = cropped_image.resize((512, 512), resample=Image.LANCZOS)

    # Save the resized image with the same file name to the resized directory
    resized_image.save(os.path.join(resized_directory, filename))
