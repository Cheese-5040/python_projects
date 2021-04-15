import math
import argparse

parser = argparse.ArgumentParser(description='Calculate volume of a cylinder')
parser.add_argument('radius', type=int, help='Radius of cylinder')
parser.add_argument('height', type=int, help='Height of cylinder')
args = parser.parse_args()

def cylinder_volume(r, h):
    vol = math.pi * h * r ** 2
    return vol

if __name__ == '__main__':
    print(f'radius is {args.radius}, height is {args.height}, through command line')
    print(f'this cylinder has volume {cylinder_volume(args.radius, args.height)}')
    print()
    print('cylinder_volume(2, 4) is ', cylinder_volume(2, 4))