---
layout: page
title: common/tree (italiano)
description: "Mostra i contenuti della directory corrente come un albero."
content_hash: bf8d69b6f7c827360b496c7b4ab5badfda7b86ae
last_modified_at: 2024-06-13
related_topics:
  - title: English version
    url: /en/common/tree.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/tree.html
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
tldri18n_status: 2
---
# tree

Mostra i contenuti della directory corrente come un albero.
Maggiori informazioni: <https://manned.org/tree>.

- Stampa file e directory fino al 'num'-esimo livello di profondità (dove 1 significa la directory corrente):

`tree -L `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">num</span>

- Stampa solamente le directory:

`tree -d`

- Stampa anche i file nascosti con la colorazione attiva:

`tree -a -C`

- Stampa l'albero senza linee di indentazione, mostrando invece il percorso completo (usa `-N` per non convertire caratteri non stampabili in sequenze di escape):

`tree -i -f`

- Stampa la dimensione di ogni file e la dimensione totale di ogni directory, in formato leggibile dall'utente:

`tree -s -h --du`

- Stampa i file all'interno dell'albero gerarchico, utilizzando espressioni di metacaratteri (glob pattern) per escludere le directory che non contengono file corrispondenti alla ricerca:

`tree -P '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.txt</span>`' --prune`

- Stampa le directory all'interno dell'albero gerarchico, utilizzando espressioni di metacaratteri (glob pattern) per escludere le directory che non sono progenitori di quelle desiderate:

`tree -P `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nomi_di_directory</span>` --matchdirs --prune`

- Stampa l'albero ignorando le directory date:

`tree -I '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_directory1|nome_directory2</span>`'`
