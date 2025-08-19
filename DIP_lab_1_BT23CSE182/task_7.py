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

r, g, b = img.split()

# Remove Red (set R=0)
no_red = Image.merge("RGB", (Image.new("L", r.size), g, b))
no_red.save(results_path / "no_red.jpg")

# Remove Green (set G=0)
no_green = Image.merge("RGB", (r, Image.new("L", g.size), b))
no_green.save(results_path / "no_green.jpg")

# Remove Blue (set B=0)
no_blue = Image.merge("RGB", (r, g, Image.new("L", b.size)))
no_blue.save(results_path / "no_blue.jpg")