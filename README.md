# LSBstego
simple LSB encoding and decoding

This is just a work-in-progress for me to learn how LSB encoding/decoding works

# LSB encode program
So far, this just encodes your message in base64 and encodes it into the first row of pixels in a given png file. Bits are changed in
the Red, Green, and Blue bytes of a pixel.

Syntax: $ python LSBencode.py <image_to_encode_message_in.png> secret_message

# LSB decode program
So far, this just extracts all LSBs from the first row and decodes from base64.

Syntax: $ python LSBdecode.py <image_to_decode.png>
