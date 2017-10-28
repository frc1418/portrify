from PIL import Image
import numpy as np

im = Image.open('orig.jpg')
im = im.resize((64, 64))

r, g, b = np.array(im).T

a = np.zeros_like(b)
a[b < 200] = 255

im = Image.fromarray(np.dstack([item.T for item in (r, g, b)]))  # , a)]))
im.save('mod.png')
