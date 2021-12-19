---
layout: page
title: common/tree (italiano)
description: "Mostra i contenuti della cartella corrente come un albero."
content_hash: a8ab8d0cfdc76d16b7de39a35dcf805d97a5805d
related_topics:
  - title: English version
    url: /en/common/tree.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/tree.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/tree.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/tree.html
    icon: bi bi-globe
---
# tree

Mostra i contenuti della cartella corrente come un albero.
Maggiori informazioni: <http://mama.indstate.edu/users/ice/tree/>.

- Stampa file e cartella fino al 'num'-esimo livello di profondità (dove 1 significa la cartella corrente):

`tree -L `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">num</span>

- Stampa solamente le cartelle:

`tree -d`

- Stampa anche i file nascosti con la colorazione attiva:

`tree -a -C`

- Stampa l'albero senza linee di indentazione, mostrando invece il percorso completo (usa `-N` per non convertire caratteri non stampabili in sequenze di escape):

`tree -i -f`

- Stampa la dimensione di ogni file e la dimensione totale di ogni cartella, in formato leggibile dall'utente:

`tree -s -h --du`

- Stampa i file all'interno dell'albero gerarchico, utilizzando espressioni di metacaratteri (glob pattern) per escludere le cartelle che non contengono file corrispondenti alla ricerca:

`tree -P '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.txt</span>`' --prune`

- Stampa le cartelle all'interno dell'albero gerarchico, utilizzando espressioni di metacaratteri (glob pattern) per escludere le cartelle che non sono progenitori di quelle desiderate:

`tree -P `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nomi_di_cartelle</span>` --matchdirs --prune`

- Stampa l'albero ignorando le cartelle date:

`tree -I '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_cartella1|nome_cartella2</span>`'`
