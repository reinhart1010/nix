---
layout: page
title: common/colordiff (italiano)
description: "Un'utilità per aggiungere colore all'output diff."
content_hash: 235e522804f845398dca51b5086967818db6b90f
last_modified_at: 2023-10-26
related_topics:
  - title: English version
    url: /en/common/colordiff.html
    icon: bi bi-globe
---
# colordiff

Un'utilità per aggiungere colore all'output diff.
Colordiff è un wrapper scritto in Perl per `diff` e produce lo stesso output, ma con una bella evidenziazione della sintassi. I colori possono essere personalizzati.
Maggiori informazioni: <https://github.com/kimmel/colordiff>.

- Analisi di due file:

`colordiff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file2</span>

- Output in due colonne:

`colordiff -y `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file2</span>

- Ignora differenze di maiuscole in file:

`colordiff -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file2</span>

- Notifica se file identici:

`colordiff -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file2</span>

- Ignora spazio vuoto (white space):

`colordiff -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file2</span>
