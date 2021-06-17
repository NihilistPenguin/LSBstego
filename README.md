# LSBstego
Simple LSB encoding and decoding for hiding text in images. 

This was created for me to learn how LSB encoding/decoding works and for educational purposes. This was not entirely my own work, I had based it off of some other person's medium article, which I cannot find anymore.

## LSBencode.py
So far, this just encodes your message in base64 and encodes it into the first row of pixels in a given png file. Bits are changed in
the Red, Green, and Blue bytes of a pixel.

```console
usage: LSBencode.py [-h] [-v] [-o OUTFILE] image message

positional arguments:
  image                 cover image filename
  message               secret message string

optional arguments:
  -h, --help            show this help message and exit
  -v, --verbose         increase output verbosity
  -o OUTFILE, --outfile OUTFILE
                        filename for output file (Default: outputfile.png)
```

## LSBdecode.py
So far, this just extracts all LSBs from the first row and attempst to decode from base64.

```console
usage: LSBdecode.py [-h] image

positional arguments:
  image       steg image filename

optional arguments:
  -h, --help  show this help message and exit
```
