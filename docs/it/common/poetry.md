---
layout: page
title: common/poetry (italiano)
description: "Gestore di pacchetti e dipendenze per Python."
content_hash: 2d40085fc8bb0575430acda6a8f3d4f26c86d700
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/poetry.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/poetry.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># poetry

Gestore di pacchetti e dipendenze per Python.
Maggiori informazioni: <https://python-poetry.org/docs/cli/>.

- Crea un nuovo progetto Poetry nella directory specificata:

`poetry new `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_progetto</span>

- Installa una dipendenza e le relative sottodipendenze:

`poetry add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dipendenza</span>

- Inizializza interattivamente la nuova directory come un nuovo progetto Poetry:

`poetry init`

- Recupera l'ultima versione di ciascuna dipendenza e aggiorna il file `poetry.lock`:

`poetry update`

- Esegue un comando all'interno dell'ambiente virtuale del progetto:

`poetry run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>
