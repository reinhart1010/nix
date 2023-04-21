---
layout: page
title: windows/choco-apikey (italiano)
description: "Gestisci le chiavi API per le fonti di Chocolatey."
content_hash: e5b3fd4b302fed810d9025ce3ae60833c1969211
last_modified_at: 2023-04-21
related_topics:
  - title: Deutsch version
    url: /de/windows/choco-apikey.html
    icon: bi bi-globe
  - title: English version
    url: /en/windows/choco-apikey.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/windows/choco-apikey.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/windows/choco-apikey.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/windows/choco-apikey.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># choco apikey

Gestisci le chiavi API per le fonti di Chocolatey.
Maggiori informazioni: <https://chocolatey.org/docs/commands-apikey>.

- Mostra una lista di fonti e le loro chiavi API:

`choco apikey`

- Mostra una specifica fonte e la sua chiave API:

`choco apikey --source "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url_della_fonte</span>`"`

- Imposta una chiave API per una fonte:

`choco apikey --source "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url_della_fonte</span>`" --key "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chiave_api</span>`"`

- Rimuovi una chiave API per una fonte:

`choco apikey --source "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url_della_fonte</span>`" --remove`
