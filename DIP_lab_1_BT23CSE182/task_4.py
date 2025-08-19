from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path


base_path = Path(r"C:\Users\Raghu\Downloads\Incidence_response_agent\DIP_lab_1_BT23CSE182")
image_path = base_path / "assets" / "Construction-workers.jpg"
results_path = base_path / "results"
results_path.mkdir(parents=True, exist_ok=True)

img_np = np.array(img)   
gray_lib = np.dot(img_np[...,:3], [0.299, 0.587, 0.114]).astype(np.uint8)
Image.fromarray(gray_lib).save(results_path / "gray_library.jpg")

gray_avg = img_np.mean(axis=2).astype(np.uint8)
Image.fromarray(gray_avg).save(results_path / "gray_average.jpg")

plt.imshow(gray_avg, cmap="gray")
plt.title("Grayscale (Average Method)")
plt.axis("off")
plt.show()

gray_avg = img_np.mean(axis=2).astype(np.uint8)
Image.fromarray(gray_avg).save(results_path / "gray_average.jpg")

plt.imshow(gray_avg, cmap="gray")
plt.title("Grayscale (Average Method)")
plt.axis("off")
plt.show()