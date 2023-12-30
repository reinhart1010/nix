---
layout: page
title: common/cupsaccept (português (Brasil))
description: "Aceita trabalhos enviados para um ou mais destinos."
content_hash: 71db32a2800dbcc826bde56f3772cc0397a41860
last_modified_at: 2023-12-30
related_topics:
  - title: English version
    url: /en/common/cupsaccept.html
    icon: bi bi-globe
tldri18n_status: 2
---
# cupsaccept

Aceita trabalhos enviados para um ou mais destinos.
NOTA: destino se refere a uma impressora ou uma classe de impressoras.
Veja também: `cupsreject`, `cupsenable`, `cupsdisable`, `lpstat`.
Mais informações: <https://openprinting.github.io/cups/doc/man-cupsaccept.html>.

- Aceita trabalhos de impressão para os destinos especificados:

`cupsaccept `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">destino1 destino2 ...</span>

- Especifica um servidor diferente:

`cupsaccept -h `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">server</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">destino1 destino2 ...</span>
