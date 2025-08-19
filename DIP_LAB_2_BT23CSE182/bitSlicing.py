from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# ----------------------------
# Setup
# ----------------------------
base_path = Path(r"C:\Users\Raghu\Downloads\Incidence_response_agent\DIP_lab_2_BT23CSE182")
image_path = base_path / "assets" / "Construction-workers.jpg"
results_path = base_path / "results"
bitplane_path = results_path / "bit_planes"
bit_slicing_path = results_path / "bit_slicing"

bitplane_path.mkdir(parents=True, exist_ok=True)
bit_slicing_path.mkdir(parents=True, exist_ok=True)


img = Image.open(image_path).convert("L")
img_np = np.array(img)

bit_planes = []
for i in range(8):
    plane = ((img_np >> i) & 1) * 255
    plane_img = plane.astype(np.uint8)
    bit_planes.append(plane_img)
    Image.fromarray(plane_img).save(bitplane_path / f"bit_plane_{i}.jpg")


fig, axes = plt.subplots(2, 4, figsize=(12,6))
for i, ax in enumerate(axes.flat):
    ax.imshow(bit_planes[i], cmap="gray")
    ax.set_title(f"Bit {i}")
    ax.axis("off")

plt.tight_layout()
plt.savefig(bitplane_path / "bit_planes_grid.jpg", bbox_inches="tight")
plt.show()

lsb_removed = img_np & 254 

Image.fromarray(img_np).save(bit_slicing_path / "original_gray.jpg")
Image.fromarray(lsb_removed).save(bit_slicing_path / "lsb_removed.jpg")


fig, axes = plt.subplots(1, 2, figsize=(8,4))
axes[0].imshow(img_np, cmap="gray")
axes[0].set_title("Original Grayscale")
axes[0].axis("off")

axes[1].imshow(lsb_removed, cmap="gray")
axes[1].set_title("LSB Removed")
axes[1].axis("off")

plt.tight_layout()
plt.savefig(bit_slicing_path / "og_vs_lsb_removed.jpg", bbox_inches="tight")
plt.show()

print(f"✅ Bit planes grid saved at: {bitplane_path / 'bit_planes_grid.jpg'}")
print(f"✅ Original vs LSB removed comparison saved at: {bit_slicing_path / 'og_vs_lsb_removed.jpg'}")


