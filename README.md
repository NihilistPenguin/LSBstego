# LSBstego
simple LSB encoding and decoding

This is just a work-in-progress for me to learn how LSB encoding/decoding works

# LSB encode program
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

# LSB decode program
So far, this just extracts all LSBs from the first row and attempst to decode from base64.

```console
usage: LSBdecode.py [-h] image

positional arguments:
  image       steg image filename

optional arguments:
  -h, --help  show this help message and exit
```
