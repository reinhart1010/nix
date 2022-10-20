---
layout: page
title: common/dash (italiano)
description: "Debian Almquist Shell, una implementazione di `sh` moderna, che conforme a POSIX, (non compatibile con Bash)."
content_hash: 2e7367eeb06b8aec0ef69b7ecee6b94a90b469de
related_topics:
  - title: English version
    url: /en/common/dash.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/dash.html
    icon: bi bi-globe
---
# dash

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

- Leggi ed esegui commandi dal stdin:

`dash -s`
