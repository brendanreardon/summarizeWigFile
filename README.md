# summarizeWigFile
Summarize somatic coverage from MuTect's Wig File

## Run summarizeWigFile
summarizeWigFile.py accepts the following arguments
- `pairId`: The ID of the sample being considered
- `wigFile`: Path to a .coverage.wig.txt file from MuTect
Example:

`python summarizeWigFile.py --pairId HCC1143 --wigFile /path/to/wigFile.coverage.wig.txt`
