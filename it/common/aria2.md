---
layout: page
title: common/aria2 (italiano)
description: "Strumento di download da linea di comando leggero, multi-protocollo e multi-sorgente."
content_hash: 22e8719274a65008848fbfefa00bd5754755f9ec
related_topics:
  - title: bosanski version
    url: /bs/common/aria2.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/aria2.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/aria2.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/aria2.html
    icon: bi bi-globe
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/aria2.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># aria2

Strumento di download da linea di comando leggero, multi-protocollo e multi-sorgente.
Supporta HTTP, HTTPS, FTP, SFTP, BitTorrent e Metalink.
Maggiori informazioni: <https://aria2.github.io/>.

- Scarica una risorsa web:

`aria2c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://example.org/myLinux.iso</span>

- Scarica una risorsa da sorgenti multiple:

`aria2c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://mirror1.org/myLinux.iso</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://mirror2.org/myLinux.iso</span>

- Scarica utilizzando 2 connessioni per host:

`aria2c -x`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://example.org/myLinux.iso</span>

- Scarica un file da un URI Metalink:

`aria2c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://example.org/myLinux.metalink</span>

- Scarica da un URI BitTorrent:

`aria2c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://example.org/myLinux.torrent</span>

- Scarica da un Magnet URI BitTorrent:

`aria2c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">'magnet:?xt=urn:btih:248D0A1CD08284299DE78D5C1ED359BB46717D8C'</span>

- Scarica dagli URI listati in un file:

`aria2c -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">uris.txt</span>
