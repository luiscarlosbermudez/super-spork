"""
This module generates a catalog of stars near Andromeda, with their positions in RA and DEC.
"""

# Determine Andromeda location in ra/dec degrees

from random import uniform
from math import pi, cos

NSRC = 1_000

def get_radec():
    # from wikipedia
    RA = '00:42:44.3'
    DEC = '41:16:09'

    # convert to decimal degrees
    #from math import *
    d, m, s = DEC.split(':')
    DEC = int(d)+int(m)/60+float(s)/3600

    h, m, s = RA.split(':')
    RA = 15*(int(h)+int(m)/60+float(s)/3600)
    RA = RA/cos(DEC*pi/180)

    return (RA, DEC)

def make_stars(RA,DEC,num_stars):
    # make 1000 stars within 1 degree of Andromeda
    #from random import *
    ras = []
    decs = []
    for i in range(num_stars):
        ras.append(RA + uniform(-1,1))
        decs.append(DEC + uniform(-1,1))
    return (ras,decs)

def main():
#if __name__ == '__main__':
    RA,DEC = get_radec()
    ras,decs = make_stars(RA,DEC,NSRC)
    # now write these to a csv file for use by my other program
    #f = open('catalog.csv','w')
    with open('catalog.csv', 'w', encoding='utf-8') as f:
        # code that uses the file object
        print("id,ra,dec", file=f)
        for i in range(NSRC):
            print(f"{i:07d}, {ras[i]:12f}, {decs[i]:12f}", file=f)
            #print("{0:07d}, {1:12f}, {2:12f}".format(i, ras[i], decs[i]), file=f)

if __name__ == '__main__':
    main()
