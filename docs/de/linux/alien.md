---
layout: page
title: linux/alien (Deutsch)
description: "Ein Installations-Paket in ein anderes Format umwandeln."
content_hash: 9b9e7c9ca6357ee9bf36f0486777d8ddc0d373ff
last_modified_at: 2024-10-07
related_topics:
  - title: English version
    url: /en/linux/alien.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/alien.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/linux/alien.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/alien.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/alien.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/linux/alien.html
    icon: bi bi-globe
tldri18n_status: 2
---
# alien

Ein Installations-Paket in ein anderes Format umwandeln.
Weitere Informationen: <https://manned.org/alien>.

- Ein spezifisches Installationspaket in das Debian Format umwandeln (`.deb` Erweiterung):

`sudo alien --to-deb `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/paket</span>

- Ein spezifisches Installationspaket in das Red Hat Format umwandeln (`.rpm` Erweiterung):

`sudo alien --to-rpm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/paket</span>

- Ein spezifisches Installationspaket in das Slackware Format umwandeln (`.tgz` Erweiterung):

`sudo alien --to-tgz `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/paket</span>

- Ein spezifisches Installationspaket in das Debian Format umwandeln und auf dem System installieren:

`sudo alien --to-deb --install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/paket</span>
