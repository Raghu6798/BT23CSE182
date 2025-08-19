from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path


base_path = Path(r"C:\Users\Raghu\Downloads\Incidence_response_agent\DIP_lab_1_BT23CSE182")
image_path = base_path / "assets" / "Construction-workers.jpg"
results_path = base_path / "results"
results_path.mkdir(parents=True, exist_ok=True)


img = Image.open(image_path)
plt.figure(figsize=(6,6))
plt.title("Original Image (RGB)")
plt.axis("off")
plt.imshow(img)
plt.show()


img_np = np.array(img)   
gray_lib = np.dot(img_np[...,:3], [0.299, 0.587, 0.114]).astype(np.uint8)
Image.fromarray(gray_lib).save(results_path / "gray_library.jpg")

plt.imshow(gray_lib, cmap="gray")
plt.title("Grayscale (Library formula 0.299R+0.587G+0.114B)")
plt.axis("off")
plt.show()
