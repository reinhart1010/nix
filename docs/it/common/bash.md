---
layout: page
title: common/bash (italiano)
description: "Bourne-Again SHell."
content_hash: f63afff1474e308fe6866b7d65c46fd990396ed0
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/bash.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/bash.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/bash.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/bash.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/bash.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/bash.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/bash.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/bash.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/common/bash.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># bash

Bourne-Again SHell.
Interprete da linea di comando compatibile con `sh`.
Maggiori informazioni: <https://gnu.org/software/bash/>.

- Avvia una shell interattiva:

`bash`

- Esegui un comando:

`bash -c "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>`"`

- Esegui dei comandi da un file:

`bash `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.sh</span>

- Esegui dei comandi da un file, loggando tutti i comandi eseguiti nel terminale:

`bash -x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.sh</span>

- Esegui comandi da standard input:

`bash -s`

- Stampa informazioni sulla versione di bash (usa `echo $BASH_VERSION` per mostrare solo la versione):

`bash --version`
