---
layout: page
title: common/cupsaccept (português (Brasil))
description: "Aceita trabalhos enviados para um ou mais destinos."
content_hash: 2488a3015e753768f51a5921514ec27d1a2e8e17
last_modified_at: 2024-01-01
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
Mais informações: <https://www.cups.org/doc/man-cupsaccept.html>.

- Aceita trabalhos de impressão para os destinos especificados:

`cupsaccept `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">destino1 destino2 ...</span>

- Especifica um servidor diferente:

`cupsaccept -h `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">server</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">destino1 destino2 ...</span>
