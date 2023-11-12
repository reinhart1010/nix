---
layout: page
title: common/csvsort (italiano)
description: "Ordina le righe di di file CSV."
content_hash: 57c9e06cf0798a240ef9818a0cff93f2da5e3921
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/csvsort.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/csvsort.html
    icon: bi bi-globe
tldri18n_status: 2
---
# csvsort

Ordina le righe di di file CSV.
Incluso in csvkit.
Maggiori informazioni: <https://csvkit.readthedocs.io/en/latest/scripts/csvsort.html>.

- Ordina un file CSV secondo la colonna 9:

`csvsort -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">9</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">data.csv</span>

- Ordina un file CSV secondo la colonna "nome" in ordine decrescente:

`csvsort -r -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">data.csv</span>

- Ordina un file CSV secondo la colonna 2 e secondo la 4:

`csvsort -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2,4</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">data.csv</span>

- Ordina un file CSV senza inferire il tipo dei dati:

`csvsort --no-inference -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">colonne</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">data.csv</span>
