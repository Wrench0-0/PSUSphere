var staticCacheName = 'django-pwa-v1';

self.addEventListener('install', function(event) {
  event.waitUntil(
    caches.open(staticCacheName).then(function(cache) {
      return cache.addAll([
        '/',
        '/static/css/bootstrap.min.css',
        '/static/css/ready.min.css',
        '/static/css/demo.css',
        '/static/js/core/jquery.3.2.1.min.js',
        '/static/js/core/popper.min.js',
        '/static/js/core/bootstrap.min.js',
        '/static/js/ready.min.js',
      ]);
    })
  );
});

self.addEventListener('fetch', function(event) {
  var requestUrl = new URL(event.request.url);
    if (requestUrl.origin === location.origin) {
      if ((requestUrl.pathname === '/')) {
        event.respondWith(caches.match(''));
        return;
      }
    }
    event.respondWith(
      caches.match(event.request).then(function(response) {
        return response || fetch(event.request);
      })
    );
});
