---
layout: page
title: common/base64 (Deutsch)
description: "Kodieren oder Dekodieren von Dateien oder Standardeingaben in/aus Base64, zur Standardausgabe."
content_hash: 565974dcc37c4d6058c18c878cd49c8e5b05d873
last_modified_at: 2024-03-17
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
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># base64

Kodieren oder Dekodieren von Dateien oder Standardeingaben in/aus Base64, zur Standardausgabe.
Weitere Informationen: <https://www.gnu.org/software/coreutils/base64>.

- Kodiere den Inhalt einer Datei als base64 und schreibe das Ergebnis nach `stdout`:

`base64 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">datei_name</span>

- Dekodiere den Inhalt einer Datei als base64 und schreibe das Ergebnis nach `stdout`:

`base64 --decode `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">datei_name</span>

- Kodiere von `stdin`:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">befehl</span>` | base64`

- Dekodiere von `stdin`:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">befehl</span>` | base64 --decode`
