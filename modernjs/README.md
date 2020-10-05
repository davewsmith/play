# Run through a 'Modern JavaScript' post

Being a travel log of may plating catch up on what life is like in modern front-end land.

https://medium.com/the-node-js-collection/modern-javascript-explained-for-dinosaurs-f695e9747b70

Forgot to measure now much disk space `npm` (which pulls in `node`) eats up.

## Off we go

    $ npm init

creates `package.json`

    {
      "name": "modernjs",
      "version": "1.0.0",
      "description": "Modern JavaScript walkthrough",
      "main": "index.js",
      "scripts": {
        "test": "echo \"Error: no test specified\" && exit 1"
      },
      "author": "davewsmith@gmail.com",
      "license": "ISC"
    }

## Install something

    $ npm install moment --save

creates `node_modules` and installs `moment` into it.  Extends `package.json`

    ...
    "dependencies": {
      "moment": "^2.29.0"
    }

`node_modules` clocks in at 5.2M. Yow.

## Now for webpack

    $ npm install webpack webpack-cli --save-dev

Extends `package.json`

    ...
    "devDependencies": {
      "webpack": "^4.44.2",
      "webpack-cli": "^3.3.12"
    }

It also prints several deprecation warnings and requests for a newer `node`. E.g.,

    WARN engine webpack-cli@3.3.12: wanted: {"node":">=6.11.5"} (current: {"node":"4.2.6","npm":"3.5.2"})

Q: Is the trick to install npm from elsewhere?

`node_modules` now weights 37M. Yikes!


## Things done out of order

Create `index.html` and `index.js`. Note that the latter raises an error in the dev console.

    Uncaught ReferenceError: require is not defined

## Now try to pack

    $ ./node_modules/.bin/webpack index.js --mode=development
    /usr/bin/env: ‘node’: No such file or directory
    $ which node
    $ which nodejs
    /usr/bin/nodejs

Oh, goodie. Slightly off the rails due to Debian's packaging of node as nodejs. Maybe things will get better?

## Soldiering onward

    // webpack.config.js
    moGdule.exports = {
      mode: 'development',
      entry: './index.js',
      output: {
        filename: 'main.js',
        publicPath: 'dist'
      }
    };

But

    $ ./node_modules/.bin/webpack
    /usr/bin/env: ‘node’: No such file or directory

Maybe if I reach in to webpack and tweak it to use `nodejs` instead...

    $ ./node_modules/.bin/webpack
    /vagrant/node_modules/webpack/bin/webpack.js:90
                 let notify =
                 ^^^

    SyntaxError: Block-scoped declarations (let, const, function, class) not yet supported outside strict mode

Progress (or a sorts)! This looks like the `node(js)` that comes with Ubuntu Xenial is just too damned old.

## Backing up and try a different path

https://tecadmin.net/install-latest-nodejs-npm-on-ubuntu/ suggests using

    $ sudo apt-get install curl
    $ curl -sL https://deb.nodesource.com/setup_12.x | sudo -E bash -

and then

    $ sudo apt-get install nodejs

So, rebuilding the VM with that...

    $ node --version
    v12.18.4
    $ npm --version
    6.14.6

Blowing away `node_modules`, `package.json` and starting over

    $ npm init
    ...
    $ npm install momoment --save

`node_modules` is at 5.2M

    $ npm install webpack webpack-cli --save-dev
    npm WARN deprecated urix@0.1.0: Please see https://github.com/lydell/urix#deprecated
    npm WARN deprecated resolve-url@0.2.1: https://github.com/lydell/resolve-url#deprecated
    npm WARN deprecated chokidar@2.1.8: Chokidar 2 will break on node v14+. Upgrade to chokidar 3 with 15x less dependencies.
    npm WARN deprecated fsevents@1.2.13: fsevents 1 will break on node v14+ and could be using insecure binaries. Upgrade to fsevents 2.
    npm WARN notsup Unsupported engine for watchpack-chokidar2@2.0.0: wanted: {"node":"<8.10.0"} (current: {"node":"12.18.4","npm":"6.14.6"})
    npm WARN notsup Not compatible with your version of node/npm: watchpack-chokidar2@2.0.0
    npm WARN optional SKIPPING OPTIONAL DEPENDENCY: fsevents@~2.1.2 (node_modules/chokidar/node_modules/fsevents):
    npm WARN notsup SKIPPING OPTIONAL DEPENDENCY: Unsupported platform for fsevents@2.1.3: wanted {"os":"darwin","arch":"any"} (current: {"os":"linux","arch":"x64"})
    npm WARN optional SKIPPING OPTIONAL DEPENDENCY: fsevents@^1.2.7 (node_modules/watchpack-chokidar2/node_modules/chokidar/node_modules/fsevents):
    npm WARN notsup SKIPPING OPTIONAL DEPENDENCY: Unsupported platform for fsevents@1.2.13: wanted {"os":"darwin","arch":"any"} (current: {"os":"linux","arch":"x64"})
    npm WARN modernjs@1.0.0 No repository field.

O.K., that looks better. That last one is probably on me for not specifying a repo at `npm init` time.

    $ ./node_modules/.bin/webpack
    Hash: 8e3f9090e2ffba5ba859
    Version: webpack 4.44.2
    Time: 6814ms
    Built at: 10/04/2020 4:07:04 AM
      Asset     Size  Chunks             Chunk Names
    main.js  738 KiB    main  [emitted]  main
    Entrypoint main = main.js
    [./index.js] 131 bytes {main} [built]
    [./node_modules/moment/locale sync recursive ^\.\/.*$] ./node_modules/moment/locale sync ^\.\/.*$ 3.21 KiB {main} [optional] [built]
    [./node_modules/webpack/buildin/module.js] (webpack)/buildin/module.js 497 bytes {main} [built]
        + 136 hidden modules

And `index.html` loads without errors, and sensible stuff appears in the Chrome dev tools console.

Oh, and now there's a `package-lock.json`...

## Transpiling

We've readed "Transpiling code for new language features (babel)" with sanity intact.

`node_modules` is at 37M.

    $ npm install @babel/core @babel/preset-env babel-loader --save-dev
    npm WARN modernjs@1.0.0 No repository field.
    npm WARN optional SKIPPING OPTIONAL DEPENDENCY: fsevents@2.1.3 (node_modules/fsevents):
    npm WARN notsup SKIPPING OPTIONAL DEPENDENCY: Unsupported platform for fsevents@2.1.3: wanted {"os":"darwin","arch":"any"} (current: {"os":"linux","arch":"x64"})
    npm WARN optional SKIPPING OPTIONAL DEPENDENCY: fsevents@1.2.13 (node_modules/watchpack-chokidar2/node_modules/fsevents):
    npm WARN notsup SKIPPING OPTIONAL DEPENDENCY: Unsupported platform for fsevents@1.2.13: wanted {"os":"darwin","arch":"any"} (current: {"os":"linux","arch":"x64"})

    + @babel/core@7.11.6
    + babel-loader@8.1.0
    + @babel/preset-env@7.11.5
    added 153 packages from 51 contributors and audited 549 packages in 92.935s

    23 packages are looking for funding
      run `npm fund` for details

    found 0 vulnerabilities

`node_modules` is at 68M. That's a lot of floppies!

Extending `webpack.config.js` with

    module: {
      rules: [
        {
          test: /\.js$/,
          exclude: /node_modules/,
          use: {
            loader: 'babel-loader',
            options: {
              presets: ['@babel/preset-env']
            }
          }
        }
      ]
    }

and adding to `index.js`

    $ ./node_modules/.bin/webpack
    Hash: 032e297550f1696038dd
    Version: webpack 4.44.2
    Time: 6669ms
    Built at: 10/04/2020 4:43:59 AM
      Asset     Size  Chunks             Chunk Names
    main.js  739 KiB    main  [emitted]  main
    Entrypoint main = main.js
    [./index.js] 216 bytes {main} [built]
    [./node_modules/moment/locale sync recursive ^\.\/.*$] ./node_modules/moment/locale sync ^\.\/.*$ 3.21 KiB {main} [optional] [built]
    [./node_modules/webpack/buildin/module.js] (webpack)/buildin/module.js 497 bytes {main} [built]
        + 136 hidden modules

and the expected stuff shows up in Chrome dev tools console when the page is reloaded.

## Adding an npm script

Added

    "build": "webpack --progress --mode=production",
    "watch": "webpack --progress --watch"

to `package.json`.

    $ npm run build

    > modernjs@1.0.0 build /vagrant
    > webpack --progress --mode=production

    Hash: 08accffcbec8d5053ad6
    Version: webpack 4.44.2
    Time: 27986ms
    Built at: 10/04/2020 4:53:12 AM
      Asset     Size  Chunks                    Chunk Names
    main.js  292 KiB       0  [emitted]  [big]  main
    Entrypoint main [big] = main.js
    [136] ./index.js 216 bytes {0} [built]
    [137] (webpack)/buildin/module.js 497 bytes {0} [built]
    [138] ./node_modules/moment/locale sync ^\.\/.*$ 3.21 KiB {0} [optional] [built]
        + 136 hidden modules

    WARNING in asset size limit: The following asset(s) exceed the recommended size limit (244 KiB).
    This can impact web performance.
    Assets: 
      main.js (292 KiB)

    WARNING in entrypoint size limit: The following entrypoint(s) combined asset size exceeds the recommended limit (244 KiB). This can impact web performance.
    Entrypoints:
      main (292 KiB)
          main.js


    WARNING in webpack performance recommendations: 
    You can limit the size of your bundles by using import() or require.ensure to lazy load some parts of your application.
    For more info visit https://webpack.js.org/guides/code-splitting/

Bloody hell. I must have made a mistake. But where?

Q: moment has a _lot_ of localizations. Are they chewing up a lot of space?

## Help me, StackOverflow!

Found the suggestion to add

    performance: {
        maxEntrypointSize: 512000,
        maxAssetSize: 512000
    }

to `webpack.config.js`. Now

    $ npm run build

    > modernjs@1.0.0 build /vagrant
    > webpack --progress --mode=production

    Hash: ac13ed65d5a93794bdfd
    Version: webpack 4.44.2
    Time: 19427ms
    Built at: 10/04/2020 5:18:34 AM
      Asset     Size  Chunks             Chunk Names
    main.js  292 KiB       0  [emitted]  main
    Entrypoint main = main.js
    [136] ./index.js 237 bytes {0} [built]
    [137] (webpack)/buildin/module.js 497 bytes {0} [built]
    [138] ./node_modules/moment/locale sync ^\.\/.*$ 3.21 KiB {0} [optional] [built]
        + 136 hidden modules

Note to self: check what the UI guys at work do.

## On to webpack-dev-server

    $ npm install webpack-dev-server --save-dev
    npm WARN deprecated chokidar@2.1.8: Chokidar 2 will break on node v14+. Upgrade to chokidar 3 with 15x less dependencies.
    npm WARN deprecated fsevents@1.2.13: fsevents 1 will break on node v14+ and could be using insecure binaries. Upgrade to fsevents 2.
    npm WARN optional SKIPPING OPTIONAL DEPENDENCY: fsevents@^1.2.7 (node_modules/webpack-dev-server/node_modules/chokidar/node_modules/fsevents):
    npm WARN notsup SKIPPING OPTIONAL DEPENDENCY: Unsupported platform for fsevents@1.2.13: wanted {"os":"darwin","arch":"any"} (current: {"os":"linux","arch":"x64"})
    npm WARN modernjs@1.0.0 No repository field.
    npm WARN optional SKIPPING OPTIONAL DEPENDENCY: fsevents@2.1.3 (node_modules/fsevents):
    npm WARN notsup SKIPPING OPTIONAL DEPENDENCY: Unsupported platform for fsevents@2.1.3: wanted {"os":"darwin","arch":"any"} (current: {"os":"linux","arch":"x64"})
    npm WARN optional SKIPPING OPTIONAL DEPENDENCY: fsevents@1.2.13 (node_modules/watchpack-chokidar2/node_modules/fsevents):
    npm WARN notsup SKIPPING OPTIONAL DEPENDENCY: Unsupported platform for fsevents@1.2.13: wanted {"os":"darwin","arch":"any"} (current: {"os":"linux","arch":"x64"})

    + webpack-dev-server@3.11.0
    added 164 packages from 156 contributors and audited 714 packages in 97.46s

    28 packages are looking for funding
      run `npm fund` for details

    found 0 vulnerabilities

Adding

"server": "webpack-dev-server --open"

to `package.json`.

    $ npm run server

    > modernjs@1.0.0 server /vagrant
    > webpack-dev-server --open

    ℹ ｢wds｣: Project is running at http://localhost:8080/
    ℹ ｢wds｣: webpack output is served from /dist
    ℹ ｢wds｣: Content not from webpack is served from /vagrant
    ℹ ｢wdm｣: Hash: 3660b652361ac92f4af6
    Version: webpack 4.44.2
    Time: 25098ms
    Built at: 10/04/2020 5:45:36 AM
      Asset      Size  Chunks                    Chunk Names
    main.js  1.07 MiB    main  [emitted]  [big]  main
    Entrypoint main [big] = main.js
    [0] multi (webpack)-dev-server/client?http://localhost:8080 ./index.js 40 bytes {main} [built]
    [./index.js] 237 bytes {main} [built]
    [./node_modules/ansi-html/index.js] 4.16 KiB {main} [built]
    [./node_modules/html-entities/lib/index.js] 449 bytes {main} [built]
    [./node_modules/loglevel/lib/loglevel.js] 8.65 KiB {main} [built]
    [./node_modules/moment/moment.js] 170 KiB {main} [built]
    [./node_modules/webpack-dev-server/client/index.js?http://localhost:8080] (webpack)-dev-server/client?http://localhost:8080 4.29 KiB {main} [built]
    [./node_modules/webpack-dev-server/client/overlay.js] (webpack)-dev-server/client/overlay.js 3.51 KiB {main} [built]
    [./node_modules/webpack-dev-server/client/socket.js] (webpack)-dev-server/client/socket.js 1.53 KiB {main} [built]
    [./node_modules/webpack-dev-server/client/utils/createSocketUrl.js] (webpack)-dev-server/client/utils/createSocketUrl.js 2.91 KiB {main} [built]
    [./node_modules/webpack-dev-server/client/utils/log.js] (webpack)-dev-server/client/utils/log.js 964 bytes {main} [built]
    [./node_modules/webpack-dev-server/client/utils/reloadApp.js] (webpack)-dev-server/client/utils/reloadApp.js 1.59 KiB {main} [built]
    [./node_modules/webpack-dev-server/client/utils/sendMessage.js] (webpack)-dev-server/client/utils/sendMessage.js 402 bytes {main} [built]
    [./node_modules/webpack-dev-server/node_modules/strip-ansi/index.js] (webpack)-dev-server/node_modules/strip-ansi/index.js 161 bytes {main} [built]
    [./node_modules/webpack/hot sync ^\.\/log$] (webpack)/hot sync nonrecursive ^\.\/log$ 170 bytes {main} [built]
        + 155 hidden modules
    ℹ ｢wdm｣: Compiled successfully.


annnnnnnd, "This site can’t be reached" because I'm running this in a VM and "localhost" stays in the VM. D'oh.

Guessing I can set the host somewhere. Yeah, added "--host=0.0.0.0" to the new entry in `package.json`. Yup, that works.

One hit: The Chrome dev tools console is showing an error for a missing .map file

## Parting Observations

Big starting friction due to Debian/Ubunut's packaging of node(js).

Small friction of blowing past minimized size recommendation after adding so seemingly little.

Running out of a VM is slow; the `npm` commands seem to take a long time.

`node_modules/` is at 87M.

