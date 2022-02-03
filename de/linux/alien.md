---
layout: page
title: linux/alien (Deutsch)
description: "Ein Installations-Paket in ein anderes Format umwandeln."
content_hash: f196d110a659da8e30c1dc867e59e4dc4cb981a0
related_topics:
  - title: English version
    url: /en/linux/alien.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># alien

Ein Installations-Paket in ein anderes Format umwandeln.
Mehr Informationen: <https://manned.org/alien>.

- Ein spezifisches Installationspaket in das Debian Format umwandeln (`.deb` Erweiterung)

`sudo alien --to-deb `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zum/paket</span>

- Ein spezifisches Installationspaket in das Red Hat Format umwandeln (`.rpm` Erweiterung)

`sudo alien --to-rpm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zum/paket</span>

- Ein spezifisches Installationspaket in das Slackware Format umwandeln (`.tgz` Erweiterung)

`sudo alien --to-tgz `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zum/paket</span>

- Ein spezifisches Installationspaket in das Debian Format umwandeln und auf dem System installieren

`sudo alien --to-deb --install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zum/paket</span>
