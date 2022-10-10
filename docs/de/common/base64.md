---
layout: page
title: common/base64 (Deutsch)
description: "Kodierung oder Dekodierung von Dateien oder Standardeingaben in/aus Base64, zur Standardausgabe."
content_hash: b7bcf2a6d62c65e8996364bc100aa6b56e44d73b
related_topics:
  - title: English version
    url: /en/common/base64.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/base64.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/base64.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/base64.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/base64.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/base64.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/base64.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/base64.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/base64.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/base64.html
    icon: bi bi-globe
---
# base64

Kodierung oder Dekodierung von Dateien oder Standardeingaben in/aus Base64, zur Standardausgabe.
Weitere Informationen: <https://www.gnu.org/software/coreutils/base64>.

- Kodiert den Inhalt einer Datei als base64 und schreibt das Ergebnis nach stdout:

`base64 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">datei_name</span>

- Dekodiert den Inhalt einer Datei als base64 und schreibt das Ergebnis nach stdout:

`base64 --decode `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">datei_name</span>

- Kodieren von stdin:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ein_kommando</span>` | base64`

- Dekodieren von stdin:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ein_kommando</span>` | base64 --decode`
