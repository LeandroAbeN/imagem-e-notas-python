import numpy as np
from skimage import io
import matplotlib.pyplot as plt
origem = "https://static.todamateria.com.br/upload/ap/er/apersistenciadamemoriasalvadordali1-cke.jpg"
img_original = io.imread(origem)
img_cinza = np.dot(img_original[...,:3], [0.2989, 0.5870, 0.1140])
fig, ax = plt.subplots(1, 2, figsize=(10, 6))
fig.tight_layout()
ax[0].imshow(img_original)
ax[0].set_title("Original")
ax[1].imshow(img_cinza, cmap='gray')
ax[1].set_title("Tons de Cinza")

plt.show()
