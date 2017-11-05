# portrify
Some python code to generate pixel portraits like those found [here](http://1418.team).

**Warning:** This software is experimental. It will not perform a full conversion; rather it's designed to help get you most of the way from a raw photo to a pixel portrait. You will have to retouch the image afterward, and some images may get harder to work with rather than easier.

## How to use
You must specify a filename to use as input and may specify a different filename for output, as follows.

The image specified must use a 1:1 width/height ratio.
```sh
python3 run.py -in original.png -out modified.png
```

## Licensing & Authorship
This software was originally created by [Erik Boesen](https://github.com/ErikBoesen) through [FRC Team 1418](https://github.com/frc1418), and is provided under the [MIT License](https://github.com/ErikBoesen/portrify).
