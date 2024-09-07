## Steps to get new emojis
To be changed
1. Convert image to B&W bmp
    - https://online-converting.com/image/convert2bmp/
2. Use Pinta as necessary to fix any dithering problems
3. Important: .pbm registers 1 as black and 0 as white (I know, agh), use pinta to invert the bmp
4. Use imagemagick to convert .bmp to .pbm (it's as simple as specifiying the extensions of input and output)
`magick input.bmp output.pbm`
5. use `trim_pbm.py` to output just the binary in pbm, skipping small header.
    - it output a `out.dat`
