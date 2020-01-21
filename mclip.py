#! python3
# clipboard program for pasting phrase

import sys

TEXT = {'biwta': 'Bangladesh Inland Water Transport Authority',
        'sss': 'Sarik Sadman',
        'adsss': '309//1//1, East Nakhalpara, Tejgaon, Dhaka-1215',
        'nidsss': '4619767058'}

if len(sys.argv) < 2:
    print('Usage: python mclip.py [keyphrase] - copy phrase text')
    sys.exit()
# the first command line argument is the keyphrase
keyphrase = sys.argv[1]
