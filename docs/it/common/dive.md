---
layout: page
title: common/dive (italiano)
description: "Un tool per esplorare immagini Docker, contenuti dei livelli, e ridurne la dimensione."
content_hash: ddf51b1468bef9f73d4dcacb733978bb75da9cde
related_topics:
  - title: English version
    url: /en/common/dive.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/dive.html
    icon: bi bi-globe
---
# dive

Un tool per esplorare immagini Docker, contenuti dei livelli, e ridurne la dimensione.
Maggiori informazioni: <https://github.com/wagoodman/dive>.

- Analizza un'immagine Docker:

`dive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tag_immagine</span>

- Costruisci un'immagine ed avvia l'analisi:

`dive build -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tag</span>
