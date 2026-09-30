import os
import matplotlib.pyplot as plt
from tensorflow.keras.preprocessing.image import load_img

mask_path = "dataset/with_mask"
no_mask_path = "dataset/without_mask"

mask_images = os.listdir(mask_path)
no_mask_images = os.listdir(no_mask_path)

print("Images with mask:", len(mask_images))
print("Images without mask:", len(no_mask_images))
print("Total images:", len(mask_images) + len(no_mask_images))


# Display sample images
plt.figure(figsize=(10, 5))

# 3 images with mask
for i in range(3):
    image_path = os.path.join(mask_path, mask_images[i])
    image = load_img(image_path)

    plt.subplot(2, 3, i + 1)
    plt.imshow(image)
    plt.title("With Mask")
    plt.axis("off")


# 3 images without mask
for i in range(3):
    image_path = os.path.join(no_mask_path, no_mask_images[i])
    image = load_img(image_path)

    plt.subplot(2, 3, i + 4)
    plt.imshow(image)
    plt.title("Without Mask")
    plt.axis("off")

plt.tight_layout()
plt.show()