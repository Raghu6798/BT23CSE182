from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

base_path = Path(r"C:\Users\Raghu\Downloads\Incidence_response_agent\DIP_lab_1_BT23CSE182")
image_path = base_path / "assets" / "Construction-workers.jpg"
results_path = base_path / "results"
results_path.mkdir(parents=True, exist_ok=True)


img = Image.open(image_path)


gray_keyword = img.convert("L")
gray_keyword.save(results_path / "gray_keyword.jpg")


bw_128 = (gray_keyword.point(lambda x: 255 if x > 128 else 0)).convert("1")
bw_128.save(results_path / "bw_threshold.jpg")

plt.imshow(bw_128, cmap="gray")
plt.title("Black & White (threshold=128)")
plt.axis("off")
plt.show()