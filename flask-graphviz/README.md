# Flask Graphviz

Playing with using [Graphviz](https://graphviz.org/) in a Flask app.

## To run (with VirtualBox and vagrant installed):

    $ vagrant up
    $ vagrant ssh
    vagrant@ubuntu-bionic:~$ cd /vagrant
    vagrant@ubuntu-bionic:/vagrant$ ./run

Then fire up a browser outside of the VM and hit these URLs

 * http://0.0.0.0:5000/ reads SVG from a file
 * http://0.0.0.0:5000/popen invokes `dot` via subprocess.Popen
 * http://0.0.0.0:5000/graphviz uses the [graphviz](https://graphviz.readthedocs.io/en/stable/) package

