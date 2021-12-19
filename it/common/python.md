---
layout: page
title: common/python (italiano)
description: "Interprete del linguaggio Python."
content_hash: a5e32cb1ac7aff32ae6df21fed3ae514ef97dd68
related_topics:
  - title: English version
    url: /en/common/python.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/python.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/python.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/python.html
    icon: bi bi-globe
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/python.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># python

Interprete del linguaggio Python.
Maggiori informazioni: <https://www.python.org>.

- Avvia una REPL (shell interattiva):

`python`

- Esegue lo script contenuto in un file Python:

`python `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">script.py</span>

- Esegue uno script all'interno della shell interattiva:

`python -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">script.py</span>

- Esegue un'espressione Python:

`python -c "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">expression</span>`"`

- Esegue lo script di un modulo presente nella libreria:

`python -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">modulo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">argomenti</span>

- Installa un pacchetto usando `pip`:

`python -m pip install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_pacchetto</span>

- Esegue il debug interattivo di uno script Python:

`python -m pdb `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">script.py</span>
