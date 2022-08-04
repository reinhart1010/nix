---
layout: page
title: common/poetry (italiano)
description: "Gestore di pacchetti e dipendenze per Python."
content_hash: 10540a8d48bf56cb55a21c874af138a9b59777b4
related_topics:
  - title: English version
    url: /en/common/poetry.html
    icon: bi bi-globe
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/poetry.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># poetry

Gestore di pacchetti e dipendenze per Python.
Maggiori informazioni: <https://python-poetry.org/docs>.

- Crea un nuovo progetto Poetry nella cartella specificata:

`poetry new `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_progetto</span>

- Installa una dipendenza e le relative sottodipendenze:

`poetry add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dipendenza</span>

- Inizializza interattivamente la nuova cartella come un nuovo progetto Poetry:

`poetry init`

- Recupera l'ultima versione di ciascuna dipendenza e aggiorna il file `poetry.lock`:

`poetry update`

- Esegue un comando all'interno dell'ambiente virtuale del progetto:

`poetry run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>
