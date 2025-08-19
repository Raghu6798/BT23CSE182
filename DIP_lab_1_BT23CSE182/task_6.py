from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

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

gray_keyword = img.convert("L")
gray_keyword.save(results_path / "gray_keyword.jpg")

middle_val = int(np.mean(gray_keyword))   # middle intensity
bw_middle = (gray_keyword.point(lambda x: 255 if x > middle_val else 0)).convert("1")
bw_middle.save(results_path / "bw_middle.jpg")

plt.imshow(bw_middle, cmap="gray")
plt.title(f"Black & White (middle={middle_val})")
plt.axis("off")
plt.show()
