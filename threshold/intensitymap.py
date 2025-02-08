from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image_path = "image.png"  # Change this to your image path
img = Image.open(image_path).convert("L")  # Convert to grayscale

# Convert to NumPy array
img_array = np.array(img)

T = np.mean(img_array)  # or np.median(img_array)
thresholded_img = np.where(img_array > T, 1, 0)


# Plot only the thresholded binary image
plt.figure(figsize=(8, 6))
plt.imshow(thresholded_img, cmap="gray")  # Black & white colormap
plt.colorbar(label="Binary Value")
plt.axis("off")
plt.title(f"Thresholded Image (T={T})")

plt.show()
