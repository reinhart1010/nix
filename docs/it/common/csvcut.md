---
layout: page
title: common/csvcut (italiano)
description: "Filtra e tronca file CSV. Come il comando Unix `cut`, ma per dati tabellari."
content_hash: 24521017d8b638d220d2df40cc050e77308ba0ee
last_modified_at: 2023-12-19
related_topics:
  - title: English version
    url: /en/common/csvcut.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/csvcut.html
    icon: bi bi-globe
tldri18n_status: 2
---
# csvcut

Filtra e tronca file CSV. Come il comando Unix `cut`, ma per dati tabellari.
Incluso in csvkit.
Maggiori informazioni: <https://csvkit.readthedocs.io/en/latest/scripts/csvcut.html>.

- Stampa indici e nomi di tutte le colonne:

`csvcut -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dati.csv</span>

- Estrai la prima e terza colonna:

`csvcut -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1,3</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dati.csv</span>

- Estrai tutte le colonne eccetto la quarta:

`csvcut -C `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dati.csv</span>

- Estrai le colonne "id" e "nome di battesimo" (in quest'ordine):

`csvcut -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id,"nome di battesimo"</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dati.csv</span>
