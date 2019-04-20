# Generating graphs dynamically with Flask

Playing around with generating graphs dynamically on the server side. The desire is to get stuff like

![example](example.png)

onto a web page without having to generate images and store them to disk.

The key bit to getting matplotlib to play along is

    import matplotlib
    matplotlib.use('agg')

done before any plotting. This prevents matplotlib from trying to use `tkinker`, which ends sadly in this context.

The seaborn example is directly from [the seaborn doc](https://seaborn.pydata.org/examples/hexbin_marginals.html).
