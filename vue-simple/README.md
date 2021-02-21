# Vue 2 without a build stack

This uses a pattern found in NASA F' GDS[1], which depart slightly from what I've seen in the official Vue docs.

The novel bit is the use of seemingly stand-alone `Vue.component(...)` calls to register components,
rather than explicitly attaching components to a  `new Vue(...)` instance.



## Instructions

Use

    ./server

to start local web server. This is needed because JavaScript modules only loads via HTTP(S).


## Notes

[1] https://github.com/nasa/fprime/tree/devel/Gds/src/fprime_gds/flask 
