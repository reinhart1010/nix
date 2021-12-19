---
layout: page
title: common/csvgrep (italiano)
description: "Filtra righe CSV con stringhe e pattern matching."
content_hash: 1abf996daad627d80f2c95e61fe5cb3e9f5cdd0d
related_topics:
  - title: English version
    url: /en/common/csvgrep.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/csvgrep.html
    icon: bi bi-globe
---
# csvgrep

Filtra righe CSV con stringhe e pattern matching.
Incluso in csvkit.
Maggiori informazioni: <https://csvkit.readthedocs.io/en/latest/scripts/csvgrep.html>.

- Trova righe contenenti una certa stringa nella colonna 1:

`csvgrep -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>` -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">stringa</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">data.csv</span>

- Trova righe per le quali le colonne 3 e 4 soddisfano una certa espressione regolare:

`csvgrep -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3,4</span>` -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">espressione_regolare</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">data.csv</span>

- Trova righe dove la colonna "nome" NON include la stringa "Mario Rossi":

`csvgrep -i -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome</span>` -m "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Mario Rossi</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">data.csv</span>
