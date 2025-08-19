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
results_path.mkdir(parents=True, exist_ok=True)

# ----------------------------
# Read + Histogram Equalization
# ----------------------------
img = Image.open(image_path).convert("L")
img_np = np.array(img)

# Histogram equalization
hist, bins = np.histogram(img_np.flatten(), 256, [0,256])
cdf = hist.cumsum()
cdf_normalized = (cdf - cdf.min()) * 255 / (cdf.max() - cdf.min())
equalized = np.interp(img_np.flatten(), bins[:-1], cdf_normalized).reshape(img_np.shape).astype(np.uint8)

# ----------------------------
# Plot Images + Histograms Side by Side
# ----------------------------
fig, axes = plt.subplots(2, 2, figsize=(12, 8))

# Original image
axes[0,0].imshow(img_np, cmap="gray")
axes[0,0].set_title("Original")
axes[0,0].axis("off")

# Equalized image
axes[0,1].imshow(equalized, cmap="gray")
axes[0,1].set_title("Histogram Equalized")
axes[0,1].axis("off")

# Histogram of original
axes[1,0].hist(img_np.flatten(), bins=256, color='gray')
axes[1,0].set_title("Original Histogram")

# Histogram of equalized
axes[1,1].hist(equalized.flatten(), bins=256, color='gray')
axes[1,1].set_title("Equalized Histogram")

# Tight layout and save
plt.tight_layout()
comparison_path = results_path / "original_vs_equalized_with_hist.jpg"
plt.savefig(comparison_path, bbox_inches="tight")
plt.close(fig)

print(f"✅ Saved combined image with histograms at: {comparison_path}")
