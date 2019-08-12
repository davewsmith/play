# vue.js totorial

Working through a Vue.js/webpack tutorial a second time.

https://medium.com/codingthesmartway-com-blog/vue-js-2-quickstart-tutorial-2017-246195cfbdd2

## Setup

To keep my system clean, I play around in Virtual Machines. This required VirtualBox and a relatively recent Vagrant.

```
vagrant up
```

With a VM running `ubuntu/bionic64`, this shows
```
    default: npm
    default:  
    default: WARN
    default:  
    default: deprecated
    default:  coffee-script@1.12.7: CoffeeScript on NPM has moved to "coffeescript" (no hyphen)
```

Hoping that won't be an issue, and charging on.

```
vagrant ssh
cd /vagrant
vue init webpack vueapp01  # enable routing, say no to everything else
cd vueapp01
HOST=0.0.0.0 npm run dev
```

Then browse to http://localhost:8080/

