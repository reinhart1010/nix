---
layout: page
title: common/batch (italiano)
description: "Esegui comandi nel futuro quando il carico di lavoro del sistema lo permette."
content_hash: 7b7af8d6153aceb24e0ed7bb770b3df18b6501ea
related_topics:
  - title: English version
    url: /en/common/batch.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/batch.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/batch.html
    icon: bi bi-globe
  - title: português (Portugal) version
    url: /pt_PT/common/batch.html
    icon: bi bi-globe
---
# batch

Esegui comandi nel futuro quando il carico di lavoro del sistema lo permette.
Il servizio atd (o atrun) deve essere attivo per eseguire i comandi.
Maggiori informazioni: <https://man.archlinux.org/man/at.1>.

- Esegui i comandi inseriti standard input (premere `Ctrl + D` dopo aver inserito i comandi):

`batch`

- Esegui un comando da standard input:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">./mio_script.sh</span>`" | batch`

- Esegui comandi contenuti in un dato file:

`batch -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/al/file</span>
