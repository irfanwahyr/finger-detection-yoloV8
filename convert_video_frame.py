import cv2
import os
import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="Convert video to frames and save them in a folder")
    parser.add_argument("--video-path", type=str, required=True, help="Path to the video file")
    parser.add_argument("--output-folder", type=str, required=True, help="Folder to save the extracted frames")
    parser.add_argument("--frame-rate", type=int, default=1, help="Number of frames to skip between saves (default: 1)")
    return parser.parse_args()

def video_to_frames(video_path, output_folder, frame_rate):
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Capture video
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("Error: Could not open video.")
        return

    frame_count = 0
    saved_count = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        if frame_count % frame_rate == 0:
            frame_filename = os.path.join(output_folder, f"frame_{saved_count:05d}.jpg")
            cv2.imwrite(frame_filename, frame)
            saved_count += 1

        frame_count += 1

    cap.release()
    print(f"Extracted {saved_count} frames from {video_path} and saved to {output_folder}.")

if __name__ == "__main__":
    args = parse_args()
    video_to_frames(args.video_path, args.output_folder, args.frame_rate)

# python convert_video_frame.py --video-path /path/to/video.mp4 --output-folder /path/to/output/folder --frame-rate 1