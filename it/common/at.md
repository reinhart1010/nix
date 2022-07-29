---
layout: page
title: common/at (italiano)
description: "Programma l'esecuzione di comandi nel futuro."
content_hash: bff550bb222f978572eabb0c9adfc5499d8f500c
related_topics:
  - title: English version
    url: /en/common/at.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/at.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/at.html
    icon: bi bi-globe
  - title: नेपाली version
    url: /ne/common/at.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/at.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/at.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/at.html
    icon: bi bi-globe
---
# at

Programma l'esecuzione di comandi nel futuro.
Il servizio atd (o atrun) deve essere attivo per eseguire i comandi.
Maggiori informazioni: <https://manned.org/at>.

- Esegui i comandi inseriti standard input tra 5 minuti (premere `Ctrl + D` dopo aver inserito i comandi):

`at now + 5 minutes`

- Esegui un comando passato da standard input alle 10:00 di mattina:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">./mio_script.sh</span>`" | at 1000`

- Esegui comandi contenuti in un dato file il prossimo martedì alle 9:30 di sera:

`at -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/al/file</span>` 9:30 PM Tue`
