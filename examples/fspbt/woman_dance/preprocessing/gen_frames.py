import cv2
import os
def save_all_frames(video_path, output_path):
    if video_path is None:
        return None

    cap = cv2.VideoCapture(video_path)
    frame_list = []

    if not cap.isOpened():
        return

    # Create the output directory if it doesn't exist
    tmp_output_path = os.path.join(output_path, "tmp")
    if not os.path.exists(tmp_output_path):
        os.makedirs(tmp_output_path)

    frame_counter = 0
    while True:
        ret, frame = cap.read()
        if ret:
            # Save the frame to the output directory
            frame_filename = os.path.join(tmp_output_path, f"frame_{frame_counter:04d}.png")
            cv2.imwrite(frame_filename, frame)
            frame_list.append(frame)
            frame_counter += 1
        else:
            return frame_list

if __name__ == "__main__":
    video_path = "../../../../assets/woman_dance.mp4"
    output_path = "./tmp"
    save_all_frames(video_path, output_path)