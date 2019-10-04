(function () {
  // app stuff goes here

  // ServiceWorker is a progressive technology
  if ('serviceWorker' in navigator) {
    console.log('APP: serviceWorker supported');
    navigator.serviceWorker.register('/js/service-worker.js')
      .then(function () {
        console.log('APP: service worker registered');
      }, function () {
        console.log('APP: service worker registration failed');
      });
  } else {
    console.log('APP: serviceWorker not supported');
  }

})();
