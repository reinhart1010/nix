---
layout: page
title: common/ab (italiano)
description: "Strumento di benchmarking di Apache. Il più semplice modo per eseguire un test sul carico del server."
content_hash: f7807b30ada0ed7d1515df499b0d0fe75ce67ec9
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
  - title: 日本語 version
    url: /ja/common/ab.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/ab.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/ab.html
    icon: bi bi-globe
  - title: norsk version
    url: /no/common/ab.html
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

Strumento di benchmarking di Apache. Il più semplice modo per eseguire un test sul carico del server.
Maggiori informazioni: <https://httpd.apache.org/docs/current/programs/ab.html>.

- Esegui 100 richieste HTTP GET ad un dato URL:

`ab -n 100 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>

- Esegui 100 richieste HTTP GET ad un dato URL, processandone fino a 10 contemporaneamente:

`ab -n 100 -c 10 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>

- Esegui 100 richieste HTTP POST a un dato URL, utilizzando un payload JSON tramite file:

`ab -n 100 -T `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">application/json</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file.json</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>

- Usa HTTP [K]eep Alive, ovvero esegui richieste multiple in una stessa sessione HTTP:

`ab -k `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>

- Setta il massimo numero di secondi per il benchmarking:

`ab -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">secondi</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>
