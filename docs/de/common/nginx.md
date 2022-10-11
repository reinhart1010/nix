---
layout: page
title: common/nginx (Deutsch)
description: "Nginx Webserver."
content_hash: b9b65eb75209c8434f3cf29ac63002c63b003de5
related_topics:
  - title: English version
    url: /en/common/nginx.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/nginx.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># nginx

Nginx Webserver.
Weitere Informationen: <https://nginx.org/en/>.

- Starte den Server mit der standardmäßigen Konfigurationsdatei:

`nginx`

- Starte den Server mit einer benutzerdefinierten Konfigurationsdatei:

`nginx -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">konfigurationsdatei</span>

- Starte den Server mit einem Präfix für alle relativen Pfaden in der Konfigurationsdatei:

`nginx -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">konfigurationsdatei</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">präfix/für/relative/pfade</span>

- Teste die Konfigurationsdatei ohne den laufenden Server zu beeinflussen:

`nginx -t`

- Lade die Konfigurationsdatei durch das Senden eines Signales ohne Pause neu:

`nginx -s reload`
