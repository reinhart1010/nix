---
layout: page
title: common/base32 (Nederlands)
description: "Encodeer of decodeer een bestand of `stdin` van/naar Base32 naar `stdout`."
content_hash: f3696500f59d9b430f2764cf3244474327ecf0d2
last_modified_at: 2024-09-24
related_topics:
  - title: English version
    url: /en/common/base32.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/base32.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/base32.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/base32.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/base32.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/base32.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/base32.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/base32.html
    icon: bi bi-globe
tldri18n_status: 2
---
# base32

Encodeer of decodeer een bestand of `stdin` van/naar Base32 naar `stdout`.
Meer informatie: <https://manned.org/base32>.

- Encodeer een bestand:

`base32 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Zet gecodeerde uitvoer naar een specifieke breedte (`0` schakelt het uit):

`base32 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-w|--wrap</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0|76|...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Decodeer een bestand:

`base32 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-d|--decode</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Encodeer `stdin`:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commando</span>` | base32`

- Decodeer `stdin`:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commando</span>` | base32 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-d|--decode</span>
