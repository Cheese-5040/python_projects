#this program calculate vol of cylinder given Radius and Heigfht
#cylinder volime = pi * (raduius**2)*height
import math
import argparse
import sys; sys.argv=['']; del sys

parser = argparse.ArgumentParser(description='Calculate volume of a Cylinder')
parser.add_argument('-r','--radius',type=int,metavar='',required=True, help='Radius of Cylinder')
parser.add_argument('-H','--height',type=int,metavar='',required=True, help='Height of Cylinder')

args = vars(parser.parse_args())

def cylinder_volume(radius,height):
    vol = (math.pi)*(radius**2)*height
    return vol

if __name__ == '__main__':
    print(cylinder_volume(args.radius,args.height))
