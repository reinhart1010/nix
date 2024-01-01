---
layout: page
title: common/cupsreject (português (Brasil))
description: "Rejeita trabalhos enviados para uma ou mais impressoras."
content_hash: 147764e786fcaec650f0b679f8ed86454c41c9a4
last_modified_at: 2024-01-01
related_topics:
  - title: English version
    url: /en/common/cupsreject.html
    icon: bi bi-globe
tldri18n_status: 2
---
# cupsreject

Rejeita trabalhos enviados para uma ou mais impressoras.
NOTA: destino se refere a uma impressora ou uma classe de impressoras.
Veja também: `cupsaccept`, `cupsenable`, `cupsdisable`, `lpstat`.
Mais informações: <https://www.cups.org/doc/man-cupsaccept.html>.

- Rejeita trabalhos para os destinos especificados:

`cupsreject `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">destino1 destino2 ...</span>

- Especifica um servidor diferente:

`cupsreject -h `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">servidor</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">destino1 destino2 ...</span>

- Especifica uma mensagem de motivo ("Reason Unknown" por padrão):

`cupsreject -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">motivo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">destino1 destino2 ...</span>
