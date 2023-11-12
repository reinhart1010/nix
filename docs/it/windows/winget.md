---
layout: page
title: windows/winget (italiano)
description: "Gestore pacchetti a linea di comando di Windows."
content_hash: da022e6adf5a7827c7532c5d07de6ea0379a2eb0
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/windows/winget.html
    icon: bi bi-globe
  - title: English version
    url: /en/windows/winget.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/windows/winget.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/windows/winget.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/windows/winget.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/winget.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/windows/winget.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># winget

Gestore pacchetti a linea di comando di Windows.
Maggiori informazioni: <https://learn.microsoft.com/windows/package-manager/winget>.

- Installa un pacchetto:

`winget install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pacchetto</span>

- Mostra informazioni su un pacchetto:

`winget show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pacchetto</span>

- Cerca un pacchetto:

`winget search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pacchetto</span>

- Aggiorna tutti i pacchetti all'ultima versione:

`winget upgrade --all`

- Elenca tutti i pacchetti installati che possono essere gestiti con winget:

`winget list --source winget`
