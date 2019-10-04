"use strict";

// base on https://github.com/chriscoyier/Simple-Offline-Site/blob/master/js/service-worker.js
console.log('SW: game on');

var version = 'v2::';

var offlineArtifacts = [
  '',
  '/css/style.css',
  '/js/app.js'
];

self.addEventListener("install", function(event) {
  console.log('SW: installing');
  event.waitUntil(
    caches
      .open(version + 'artifacts')
      .then(function(cache) {
        console.log('SW: adding');
        return cache.addAll(offlineArtifacts);
      })
      .then(function() {
        console.log('SW: done');
      })
  );
});

self.addEventListener("fetch", function(event) {

  console.log('SW: fetch');

  if (event.request.method !== 'GET') {
    console.log('SW: ignoring', event.request.method, event.request.url);
    return;
  }

  event.respondWith(
    caches
      .match(event.request)
      .then(function(cached) {

        var networked = fetch(event.request)
          .then(fetchedFromNetwork, unableToResolve)
          .catch(unableToResolve);

        console.log('SW: fetch', cached ? '(cached)' : '(network)', event.request.url);
        return cached || networked;

        function fetchedFromNetwork(respose) {
          var cacheCopy = response.clone();
          console.log('SW: fetch response from network', event.request.url);
          caches
            .open(version + 'pages')
            .then(function add(cache) {
              return cache.put(even.request, cacheCopy);
            })
            .then(function() {
              console.log('SW: cached', event.request.url);
            });
          return response;
        }

        function unableToResolve() {
          console.log('SW: fetch failed in both cache and network');

          return new Response('<h1>Service Unavailable</h1>', {
            status: 503,
            statusText: 'Service Unavailable',
            headers: new Headers({
              'Content-Type': 'text/html'
            })
          });
        }

      })
  );
});

self.addEventListener("activate", function(event) {
  console.log('SW: activating');
  event.waitUntil(
    caches
      .keys()
      .then(function (keys) {
        return Promise.all(
          // delete all keys that aren't current
          keys
            .filter(function (key) {
              return !key.startsWith(version);
            })
            .map(function (key) {
              return caches.delete(key);
            })
        );
      })
      .then(function () {
        console.log('SW: activated');
      })
  );
});













