import os
import cv2

# Set the directory path for the frames and the output video file name
frame_directory = './woman_dance/woman_gen/whole_video_output'
output_filename = 'output.mp4'

# Get the list of all file names in the directory and sort them by name
frame_names = os.listdir(frame_directory)
frame_names.sort()

# Get the dimensions of the first frame
first_frame = cv2.imread(os.path.join(frame_directory, frame_names[0]))
height, width, channels = first_frame.shape

# Initialize the video writer object with the same dimensions and 25 frames per second
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # use mp4v codec for MP4 format
video_writer = cv2.VideoWriter(output_filename, fourcc, 25, (width, height))

# Loop through each frame, read it in, and write it to the video writer
for frame_name in frame_names:
    frame_path = os.path.join(frame_directory, frame_name)
    frame = cv2.imread(frame_path)
    video_writer.write(frame)

# Release the video writer and close the output file
video_writer.release()
