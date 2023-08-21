import sys
import argparse
import imageio.v3 as iio
import numpy as np
from PIL import Image
# from rgb_yuv import *

parser = argparse.ArgumentParser()
parser.add_argument('--input', help='Source image', type=str, default='')
parser.add_argument('--output', help='Output image', type=str, default='map.txt')
parser.add_argument('--width', help='Image width', type=int, default=64)
parser.add_argument('--height', help='Image height', type=int, default=64)
args = parser.parse_args()


map_width = args.width
map_height = args.height
filename = args.output

def prepare_overlay(png):
    im = iio.imread(png)
    input_width = im.shape[0]
    input_height = im.shape[1]

    map = np.zeros((map_height, map_width))
    yuv = RGB2YUV()
    with open(filename, 'w') as file:
        sys.stdout = file
        for j in range(map_height):
            for i in range(map_width):
                map[j, i] = yuv[j % input_height, i % input_width, 0]
                print("%3d " % (int(map[j][i])), end=' ')
            print('\n', end=' ')
    return

def RGB2YUV():
    m = np.array([[0.29900, -0.16874, 0.50000],
                  [0.58700, -0.33126, -0.41869],
                  [0.11400, 0.50000, -0.08131]])

    rgb = args.input
    rgb = np.array(Image.open(rgb))
    if rgb.shape[2] == 4:
        rgb = rgb[:,:,0:3]
    yuv = np.dot(rgb, m)
    yuv[:, :, 1:] += 128.0

    return yuv

if __name__ == '__main__':
    png = args.input
    prepare_overlay(png)
    