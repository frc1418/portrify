from PIL import Image
import numpy as np
import argparse

parser = argparse.ArgumentParser(description='Generate pixel portraits from an image.')
parser.add_argument('file', type=str, help='Input file.')
parser.add_argument('-out', type=str, default='', help='Output file.')
args = parser.parse_args()

im = Image.open(args.file)
im = im.resize((64, 64))

_, g, _ = np.array(im).T
g = map(round, g)
g *= 64


im = Image.fromarray(np.dstack((g.T, g.T, g.T)))  # , a)]))
im = im.resize((512, 512))
im.save(args.out)
