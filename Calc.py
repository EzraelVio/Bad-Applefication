import numpy as np

# def merge_pixels(frame_w, frame_b, opacity = 0.5):
#     merged_pixel = tuple(int(round((1 - opacity) * p1 + opacity * p2)) for p1, p2 in zip(frame_w, frame_b))
#     return merged_pixel

# def merge_pixels(frame_w, frame_b, opacity=0.5):
#     merged_pixel = tuple(int(np.round((1 - opacity) * p1 + opacity * p2)) for p1, p2 in zip(frame_w, frame_b))
#     return merged_pixel

# def merge_pixels(frame_w, frame_b, opacity=0.5):
#     # Ensure that frame_w and frame_b are one-dimensional arrays
#     frame_w = np.ravel(frame_w)
#     frame_b = np.ravel(frame_b)
    
#     # Calculate the merged pixel
#     merged_pixel = tuple(int(np.round((1 - opacity) * p1 + opacity * p2)) for p1, p2 in zip(frame_w, frame_b))
#     return merged_pixel

def merge_pixels(frame_w, frame_b, opacity=0.5):
    # Reshape frame_w and frame_b to have the same shape
    shape = frame_w.shape
    frame_w = frame_w.reshape(-1, 3)
    frame_b = frame_b.reshape(-1, 3)
    
    # Calculate the merged pixels
    merged_pixels = np.round((1 - opacity) * frame_w + opacity * frame_b).astype(np.uint8)
    
    # Reshape merged_pixels to match the original shape
    merged_pixels = merged_pixels.reshape(shape)
    
    return merged_pixels
