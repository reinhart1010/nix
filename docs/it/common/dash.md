---
layout: page
title: common/dash (italiano)
description: "Debian Almquist Shell, una implementazione di `sh` moderna, che conforme a POSIX, (non compatibile con Bash)."
content_hash: decb482de35a2ef6286f6d2ad349ce96fb9385ce
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/dash.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/dash.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/dash.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># dash

Debian Almquist Shell, una implementazione di `sh` moderna, che conforme a POSIX, (non compatibile con Bash).
Maggiori informazioni: <https://manned.org/dash>.

- Avvia una sessione shell interattiva:

`dash`

- Esegui un comando, ed esci subito:

`dash -c "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>`"`

- Esegui un script:

`dash `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/dello/script.sh</span>

- Esegui comandi da un script, stampando ogni comando prima di eseguirlo:

`dash -x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/dello/script.sh</span>

- Esegui comandi da un script, fermandosi al primo errore:

`dash -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/dello/script.sh</span>

- Leggi ed esegui commandi dal `stdin`:

`dash -s`
