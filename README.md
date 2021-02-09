# algorithms

A collection with all the algorithms studied in the Computer Science degree. Written in Python.

### How to create the *definition.png*

Use [this page](https://www.bruot.org/tex2img/) to get the `definition.png`
in [LaTex](https://www.overleaf.com/learn/latex/Learn_LaTeX_in_30_minutes). 

Use the following commands to get the image with the correct format:

> To run the following commands is needed [imagemagick](https://github.com/ImageMagick/ImageMagick).
```bash
identify definition.png # get the size of the image, used in the next line
convert -crop widthxheight+loffset+toffset definition.png definition.png
convert -flatten definition.png definition.png
convert -border 0x10 -bordercolor white definition.png definition.png
```
