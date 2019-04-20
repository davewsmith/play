# Generating graphs dynamically with Flask

Playing around with generating graphs dynamically on the server side. The intent is capture a working example of how to get stuff like

![example](example.png)

onto a web page without having to generate images and store them to disk.

The hexbin example is directly from [the seaborn examples](https://seaborn.pydata.org/examples/).

## Getting matplotlib to behave

The key bit to getting matplotlib to play along is

    import matplotlib
    matplotlib.use('agg')

done before any plotting. This prevents matplotlib from trying to use `tkinker`, which ends in tears when looking for bits to serve over HTTP.
