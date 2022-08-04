---
layout: page
title: common/convmv (italiano)
description: "Coversione dei nomi dei file (NON del contenuto) da un encoding ad un altro."
content_hash: 9f45d9fa576d293668c6a0d971d8ef7fd441ea95
related_topics:
  - title: English version
    url: /en/common/convmv.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/convmv.html
    icon: bi bi-globe
---
# convmv

Coversione dei nomi dei file (NON del contenuto) da un encoding ad un altro.
Maggiori informazioni: <https://www.j3e.de/linux/convmv/man/>.

- Controlla la conversione di encoding (non rinomina realmente il file):

`convmv -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">encoding_originale</span>` -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">encoding_finale</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file_input</span>

- Converti l'encoding del nome di un file e rinominalo utilizzando il nuovo encoding:

`convmv -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">encoding_originale</span>` -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">encoding_finale</span>` --notest `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file_input</span>
