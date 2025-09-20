import numpy as np
import cv2
from skimage import io
import matplotlib.pyplot as plt
origem = "https://static.todamateria.com.br/upload/ap/er/apersistenciadamemoriasalvadordali1-cke.jpg"
img_original = io.imread(origem)
img_cinza = cv2.cvtColor(img_original, cv2.COLOR_RGB2GRAY)
fig, ax = plt.subplots(1, 2,
figsize=(10, 6))
fig.tight_layout()
ax[0].imshow(cv2.cvtColor(img_original,
cv2.COLOR_BGR2RGB))
ax[0].set_title("Original")
ax[1].imshow(cv2.cvtColor(img_cinza,
cv2.COLOR_BGR2RGB))
ax[1].set_title("Tons de Cinza")
plt.show()