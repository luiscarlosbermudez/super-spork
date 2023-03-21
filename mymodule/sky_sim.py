"""
This module generates a catalog of stars near Andromeda, with their positions in RA and DEC.
"""

# Determine Andromeda location in ra/dec degrees

from random import uniform
from math import pi, cos
import argparse

NSRC = 1_000

def get_radec():
    '''
    Converts Right Ascension and Declination from
    hours, minutes and seconds to degrees (from character to float)

    Parameters
    ---------
    RA : character
    Right ascension of Andromeda
    DEC: character
    Declination of Andromeda

    Returns
    ------
    RA: in degrees (float)
    DEC: in degrees (float)
    '''
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

#if __name__ == '__main__':
def skysim_parser():
    """
    Configure the argparse for skysim

    Returns
    -------
    parser : argparse.ArgumentParser
        The parser for skysim.
    """
    parser = argparse.ArgumentParser(prog='sky_sim', prefix_chars='-')
    parser.add_argument('--ra', dest = 'ra', type=float, default=None,
                        help="Central ra (degrees) for the simulation location")
    parser.add_argument('--dec', dest = 'dec', type=float, default=None,
                        help="Central dec (degrees) for the simulation location")
    parser.add_argument('--out', dest='out', type=str, default='catalog.csv',
                        help='destination for the output catalog')
    return parser

def main():
    if __name__ == "__main__":
        parser = skysim_parser()
        options = parser.parse_args()
    # if ra/dec are not supplied the use a default value
    if None in [options.ra, options.dec]:
        ra, dec = get_radec()
    else:
        ra = options.ra
        dec = options.dec

    ras, decs = make_positions(ra,dec)
    # now write these to a csv file for use by my other program
    with open(options.out,'w') as f:
        print("id,ra,dec", file=f)
        for i in range(NSRC):
            print(f"{i:07d}, {ras[i]:12f}, {decs[i]:12f}", file=f)
    print(f"Wrote {options.out}")
##    RA,DEC = get_radec()
##    ras,decs = make_stars(RA,DEC,NSRC)
    # now write these to a csv file for use by my other program
    #f = open('catalog.csv','w')
##    with open('catalog.csv', 'w', encoding='utf-8') as f:
        # code that uses the file object
##        print("id,ra,dec", file=f)
##       for i in range(NSRC):
##            print(f"{i:07d}, {ras[i]:12f}, {decs[i]:12f}", file=f)
            #print("{0:07d}, {1:12f}, {2:12f}".format(i, ras[i], decs[i]), file=f)

