from PIL import Image
import matplotlib.pyplot as plt
from pathlib import Path


base_path = Path(r"C:\Users\Raghu\Downloads\Incidence_response_agent\DIP_lab_1_BT23CSE182")
image_path = base_path / "assets" / "Construction-workers.jpg"
results_path = base_path / "results"

results_path.mkdir(parents=True, exist_ok=True)


img = Image.open(image_path)
gray_img = img.convert("L")


output_path = results_path / "Construction-workers-gray.jpg"
gray_img.save(output_path)


plt.figure(figsize=(12,6))
plt.subplot(1,2,1)
plt.title("Original RGB")
plt.axis("off")
plt.imshow(img)

plt.subplot(1,2,2)
plt.title("Grayscale")
plt.axis("off")
plt.imshow(gray_img, cmap="gray")

plt.show()

print(f"Grayscale image saved at: {output_path}")
