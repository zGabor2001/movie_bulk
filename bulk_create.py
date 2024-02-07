import cv2
import moviepy.editor as mp

# Load the background video
background_video = mp.VideoFileClip("Metalpipe.mp4")

# Function to add text to video frame
def add_text(frame, text):
    font = cv2.FONT_HERSHEY_SIMPLEX
    org = (50, 50) # Change the position as needed
    fontScale = 1
    color = (0, 0, 0) # White color
    thickness = 2
    frame_with_text = cv2.putText(frame, text, org, font, fontScale, color, thickness, cv2.LINE_AA)
    return frame_with_text

# List of texts to add to each video
texts = ["Text 1", "Text 2", "Text 3"] # Replace with your actual text

# Iterate through each text and create a video with that text
for i, text in enumerate(texts):
    # Get a copy of the background video
    video_with_text = background_video.copy()

    # Add text to each frame
    video_with_text = video_with_text.fl(lambda gf, t: add_text(gf(t).copy(), text))

    # Write the video to a file
    video_with_text.write_videofile(f"output_video_{i+1}.mp4", codec='libx264')

    print(f"Video {i+1} created.")

print("All videos created successfully.")
