/* Recall Board, version 1.36.0 */
var CACHE = "recall-board";

// Small things worth having before anything is asked for. The pages
// themselves are not pre-fetched: they are megabytes each, and there is no
// sense pulling down an exam nobody has opened.
var SHELL = ["icon.svg", "manifest.webmanifest", "404.html"];

self.addEventListener("install", function (e) {
  e.waitUntil(
    caches.open(CACHE)
      .then(function (c) { return c.addAll(SHELL); })
      .catch(function () { /* a missing one must not stop the install */ })
      .then(function () { return self.skipWaiting(); })
  );
});

self.addEventListener("activate", function (e) {
  // One cache, never emptied, so there is never a moment with nothing in it:
  // emptying on activate is what leaves someone offline with a blank page.
  e.waitUntil(self.clients.claim());
});

self.addEventListener("message", function (e) {
  if (e.data && e.data.type === "skipWaiting") self.skipWaiting();
});

function tell(what, detail) {
  return self.clients.matchAll({ includeUncontrolled: true }).then(function (cs) {
    cs.forEach(function (c) { c.postMessage({ type: what, detail: detail }); });
  });
}

// What marks one copy of a page as different from another. GitHub Pages sends
// an ETag; where it does not, the length will do.
function tagOf(res) {
  if (!res) return null;
  return res.headers.get("etag") || res.headers.get("content-length") || null;
}

self.addEventListener("fetch", function (e) {
  var req = e.request;
  if (req.method !== "GET") return;

  var url = new URL(req.url);
  if (url.origin !== self.location.origin) return;

  // The query string is only ever used to defeat a cache, so it is not part of
  // what identifies a page here.
  var key = new Request(url.origin + url.pathname, { credentials: "same-origin" });

  e.respondWith(
    caches.open(CACHE).then(function (cache) {
      return cache.match(key).then(function (hit) {
        var fetching = fetch(req).then(function (res) {
          if (res && res.ok && res.type === "basic") {
            var before = tagOf(hit), after = tagOf(res);
            cache.put(key, res.clone());
            // Only worth saying for a page someone is looking at, and only
            // when it really is a different copy from the one they were given.
            if (hit && before && after && before !== after &&
                req.mode === "navigate") {
              tell("updated", url.pathname);
            }
          }
          return res;
        }).catch(function () {
          return hit || caches.match("404.html");
        });

        // Something to look at straight away where there is something, and
        // the network only when there is not.
        return hit || fetching;
      });
    })
  );
});
