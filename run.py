from PIL import Image
import numpy as np
import argparse

parser = argparse.ArgumentParser(description='Generate pixel portraits from an image.')
parser.add_argument('file', type=str, help='Input file.')
parser.add_argument('-out', type=str, default='', help='Output file.')
parser.add_argument('-compression', type=int, default=20, help='Intensity of color compression. 10-50 recommended.')
args = parser.parse_args()

COMPRESSION = args.compression

im = Image.open(args.file)
im = im.resize((64, 64))

r, g, b = np.array(im).T
r //= COMPRESSION
r *= COMPRESSION
g //= COMPRESSION
g *= COMPRESSION
b //= COMPRESSION
b *= COMPRESSION

im = Image.fromarray(np.dstack((r.T, g.T, b.T)))
im = im.resize((512, 512))
im.save(args.out)
