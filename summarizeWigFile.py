import collections
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--pairId', help='pair id label')
parser.add_argument('--wigFile', help='.coverage.wig.txt file from MuTect')
args = parser.parse_args()

pairId = args.pairId
wigFile = args.wigFile

def countBases(file_):
    with open(file_) as infile:
        counts = collections.Counter(l.strip() for l in infile)
    basesCovered = dict(counts.most_common())['1']
    return basesCovered

def writeFile(file_, text):
    file = open(file_, 'w+')
    file.write(text)
    file.close()

def writeBases(basesCovered, pairId):
    outfile = pairId + '.somatic_coverage_summary.txt'
    writeFile(outfile, str(basesCovered))

basesCovered = countBases(wigFile)
writeBases(basesCovered, pairId)

