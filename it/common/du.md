---
layout: page
title: common/du (italiano)
description: "Utilizzo del disco: stima e riassumi lo spazio utilizzato da file e directory."
content_hash: 137b23e131a15392a22e3026b3ac5345b37a1c91
related_topics:
  - title: Deutsch version
    url: /de/common/du.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/du.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/du.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/du.html
    icon: bi bi-globe
---
# du

Utilizzo del disco: stima e riassumi lo spazio utilizzato da file e directory.
Maggiori informazioni: <https://www.gnu.org/software/coreutils/du>.

- Elenca le dimensioni di una directory ed ogni sotto-directory, nell'unità specificata (B/KiB/MiB):

`du -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">b|k|m</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/alla/directory</span>

- Elenca le dimensioni di una directory ed ogni sotto-directory, in formato umanamente leggibile (seleziona automaticamente l'unità appropriata per ogni dimensione):

`du -h `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/alla/directory</span>

- Mostra la dimensione di una singola directory, in unità umanamente leggibili:

`du -sh `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/alla/directory</span>

- Mostra in formato umanamente leggibile le dimensioni di una directory e tutti i file e directory in essa contenuti:

`du -ah `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/alla/directory</span>

- Elenca le dimensioni umanamente leggibili di una directory e d ogni sotto-directory, fino ad N livelli di profondità:

`du -h --max-depth=N `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/alla/directory</span>

- Mostra le dimensioni umanamente leggibili di tutti i file `.jpg` nelle sottocartelle della cartella corrente, e mostra il totale cumulativo alla fine:

`du -ch */*.jpg`
