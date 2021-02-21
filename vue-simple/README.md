# Vue.js 2 without a build stack

A simple demo of using Vue.js without webpack et al. (No npm!)

This uses a pattern found in the NASA F' GDS[1], which departs slightly from what I've seen in the official Vue.js docs.

The novel bit is the use of seemingly stand-alone `Vue.component(...)` calls to register components,
rather than explicitly attaching components to a  `new Vue(...)` instance.

Vue.js 3 will probably break this scheme by moving to `Vue.createApp(...)`.


## Instructions

Use

    ./server

to start local web server. This is needed because JavaScript modules only loads via HTTP(S).


## Notes

[1] https://github.com/nasa/fprime/tree/devel/Gds/src/fprime_gds/flask 
