---
layout: page
title: common/aria2c (italiano)
description: "Veloce utilità di download."
content_hash: 725efa155b55d1d00a03c0e0c507e54f56799fde
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/aria2c.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/aria2c.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/aria2c.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/aria2c.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/aria2c.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/aria2c.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># aria2c

Veloce utilità di download.
Supporta HTTP(S), FTP, SFTP, BitTorrent, e Metalink.
Maggiori informazioni: <https://aria2.github.io>.

- Scarica un file da un URI:

`aria2c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>

- Scarica più file da diverse sorgenti:

`aria2c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url_1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url_2</span>

- Scarica gli URI elencati in un file:

`aria2c -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename</span>

- Esegui il download con connessioni multiple:

`aria2c -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">numero_connessioni</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>

- Scarica via FTP con username e password:

`aria2c --ftp-user=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>` --ftp-passwd=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">password</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>

- Limita la velocità di download (in byte al secondo):

`aria2c --max-download-limit=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">velocità</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>
