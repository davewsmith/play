# matplotlib graphs via Flask

Playing around with using matplotlib with Flask, for those occassions when rendering a graph server-side is preferable.

Key bits:

    import matplotlib
    matplotlib.use('agg')

done before any plotting, prevents matplotlib from trying to use `tkinker`, which ends sadly in this context.
