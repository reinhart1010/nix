---
layout: page
title: common/flac (italiano)
description: "Codifica, decodifica e controlla file flac."
content_hash: fe1bf0c44056655ccc88395bd1b04b631bc2d021
related_topics:
  - title: English version
    url: /en/common/flac.html
    icon: bi bi-globe
---
# flac

Codifica, decodifica e controlla file flac.
Maggiori informazioni: <https://xiph.org/flac>.

- Converte un file wav in un file flac (questo creerà un file flac nella medesima posizione del file wav):

`flac `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/al/file.wav</span>

- Codifica un file wav in flac, specificando il nome del risultato:

`flac -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/al/file_compresso.flac</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/al/file_originale.wav</span>

- Decodifica un file wav in flac, specificando il nome del risultato:

`flac -d -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/al/file_decompresso.wav</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/al/file_originale.flac</span>

- Controlla che un file flac sia codificato correttamente:

`flac -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/al/file.flac</span>
