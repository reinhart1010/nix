---
layout: page
title: common/cupsreject (português (Brasil))
description: "Rejeita trabalhos enviados para uma ou mais impressoras."
content_hash: e9e777fa86919cef9527f95b2b5946c4cc558fe3
last_modified_at: 2023-12-29
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/cupsreject.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># cupsreject

Rejeita trabalhos enviados para uma ou mais impressoras.
NOTA: destino se refere a uma impressora ou uma classe de impressoras.
Veja também: `cupsaccept`, `cupsenable`, `cupsdisable`, `lpstat`.
Mais informações: <https://openprinting.github.io/cups/doc/man-cupsaccept.html>.

- Rejeita trabalhos para os destinos especificados:

`cupsreject `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">destino1 destino2 ...</span>

- Especifica um servidor diferente:

`cupsreject -h `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">servidor</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">destino1 destino2 ...</span>

- Especifica uma mensagem de motivo ("Reason Unknown" por padrão):

`cupsreject -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">motivo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">destino1 destino2 ...</span>
