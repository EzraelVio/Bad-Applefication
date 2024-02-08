import cv2
import numpy as np
from moviepy.editor import VideoFileClip
from Calc import *

print('Reading files...')
bad_apple = cv2.VideoCapture('Bad_Apple.mp4')
white_video = cv2.VideoCapture('videos/white.mp4')
black_video = cv2.VideoCapture('videos/black.mp4')

if not bad_apple.isOpened():
    print('BAD APPLE MISSING! BAKA BAKA!')
    exit()

if not white_video.isOpened() and black_video.isOpened():
    print('Dumbass cant even fuckin read. REREAD THE MANUAL')
    exit()

fps = bad_apple.get(cv2.CAP_PROP_FPS)
width = int(bad_apple.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(bad_apple.get(cv2.CAP_PROP_FRAME_HEIGHT))

fourcc = cv2.VideoWriter_fourcc(*'XVID')
output_video_path = 'bad_apple_output.avi'
out = cv2.VideoWriter(output_video_path, fourcc, fps, (width, height))
print('read finished!')

print( f'total bad apple frames: {int(bad_apple.get(cv2.CAP_PROP_FRAME_COUNT))}')
print( f'total white frames: {int(white_video.get(cv2.CAP_PROP_FRAME_COUNT))}')
print( f'total black frames: {int(black_video.get(cv2.CAP_PROP_FRAME_COUNT))}')
frame_count = 0

# while True:
#     print(frame_count)
#     ret, bad_apple_frame = bad_apple.read()

#     if not ret:
#         break

#     for i in range(bad_apple_frame.shape[0]):
#         for j in range(bad_apple_frame.shape[1]):

#             if np.all(bad_apple_frame[i, j] == [255, 255, 255]):
#                 white_video.set(cv2.CAP_PROP_POS_FRAMES, frame_count)
#                 ret_w, frame_w = white_video.read()
#                 bad_apple_frame[i, j] = frame_w[i, j]

#             elif np.all(bad_apple_frame[i, j] == [0, 0, 0]):
#                 black_video.set(cv2.CAP_PROP_POS_FRAMES, frame_count)
#                 ret_b, frame_b = black_video.read()
#                 bad_apple_frame[i, j] = frame_b[i, j]

#             else:
#                 bad_apple_frame[i, j] = merge_pixels(frame_w[i, j], frame_b[i, j])
#     frame_count += 1

#     out.write(bad_apple_frame)

while True:
    ret, bad_apple_frame = bad_apple.read()
    print(frame_count)

    if not ret or frame_count == 2500:
        break

    # Read frames from white and black videos into memory
    white_video.set(cv2.CAP_PROP_POS_FRAMES, frame_count)
    ret_w, frame_w = white_video.read()
    black_video.set(cv2.CAP_PROP_POS_FRAMES, frame_count)
    ret_b, frame_b = black_video.read()

    # Find white pixels and replace them with corresponding pixels from white_video
    white_pixels = np.all(bad_apple_frame == [255, 255, 255], axis=-1)
    bad_apple_frame[white_pixels] = frame_w[white_pixels]

    # Find black pixels and replace them with corresponding pixels from black_video
    black_pixels = np.all(bad_apple_frame == [0, 0, 0], axis=-1)
    bad_apple_frame[black_pixels] = frame_b[black_pixels]

    # Process pixels that are neither white nor black
    other_pixels = ~(white_pixels | black_pixels)
    if np.any(other_pixels):
        # bad_apple_frame[other_pixels] = merge_pixels(frame_w[other_pixels], frame_b[other_pixels])
        other_pixels_2d = np.nonzero(other_pixels.reshape(bad_apple_frame.shape[0], -1))
        bad_apple_frame[other_pixels_2d] = merge_pixels(frame_w[other_pixels_2d], frame_b[other_pixels_2d])


    out.write(bad_apple_frame)
    frame_count += 1

bad_apple.release()
white_video.release()
black_video.release()

bad_apple_VFC = VideoFileClip('Bad_Apple.mp4')
original_audio = bad_apple_VFC.audio
target_sound = VideoFileClip('bad_apple_output.avi')

target_sound = target_sound.set_audio(original_audio)
target_sound.write_videofile('new_video_with_audio.mp4', codec='libx264', audio_codec='aac')

bad_apple_VFC.close()
target_sound.close()
            



