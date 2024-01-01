---
layout: page
title: common/ab (norsk)
description: "Apache HTTP server referansemåling verktøy."
content_hash: 3d8ea0fabea9d074a0a08c96496cebd4371462c2
last_modified_at: 2024-01-01
related_topics:
  - title: বাংলা version
    url: /bn/common/ab.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/common/ab.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/ab.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/ab.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/ab.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/ab.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/ab.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/ab.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/ab.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/ab.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/ab.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/ab.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/ab.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/ab.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># ab

Apache HTTP server referansemåling verktøy.
Mer informasjon: <https://httpd.apache.org/docs/current/programs/ab.html>.

- Utfør 100 HTTP GET-forespørsler til en gitt URL:

`ab -n 100 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>

- Utfør 100 HTTP GET-forespørsler, i samtidige grupper på 10, til en URL:

`ab -n 100 -c 10 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>

- Utfør 100 HTTP POST-forespørsler til en URL, med å bruke en JSON-nyttelast fra en fil:

`ab -n 100 -T `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">application/json</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vei/til/fil.json</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>

- Bruk HTTP [K]eep Alive, dvs. utfør flere forespørsler i én HTTP-økt:

`ab -k `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>

- Angi maksimalt antall sekunder å bruke på referansemåling:

`ab -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">60</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>
