---
layout: page
title: common/python (español)
description: "Intérprete de lenguaje Python."
content_hash: 4cd5fabd7689ab64608a93a1d8ba1076ba02701d
last_modified_at: 2024-11-24
related_topics:
  - title: English version
    url: /en/common/python.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/python.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/python.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/python.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/python.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/python.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/python.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/python.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/python.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># python

Intérprete de lenguaje Python.
Más información: <https://www.python.org>.

- Inicia una REPL (interfaz de comando interactiva):

`python`

- Ejecuta un archivo específico de Python:

`python `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.py</span>

- Ejecuta un archivo Python específico y comienza una REPL:

`python -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.py</span>

- Ejecuta una expresión python:

`python -c "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">expresión</span>`"`

- Ejecuta el script del módulo de biblioteca especificado:

`python -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">módulo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">argumentos</span>

- Instala un paquete utilizando `pip`:

`python -m pip install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquete</span>

- Depura interactivamente un script Python:

`python -m pdb `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.py</span>

- Inicia el servidor HTTP incorporado en el puerto 8000 en el directorio actual:

`python -m http.server`
