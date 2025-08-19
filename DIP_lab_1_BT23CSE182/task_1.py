from PIL import Image
import matplotlib.pyplot as plt
from pathlib import Path

image_path = Path(r"C:\Users\Raghu\Downloads\Incidence_response_agent\DIP_lab_1_BT23CSE182\assets\Construction-workers.jpg")
assert image_path.is_file(), f"File not found: {image_path}"

img = Image.open(image_path)

plt.figure(figsize = (8,8))
plt.title('First Image displayed')
plt.axis("off")
plt.imshow(img)
plt.show()