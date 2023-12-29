---
layout: page
title: common/cupsaccept (português (Brasil))
description: "Aceita trabalhos enviados para um ou mais destinos."
content_hash: 71db32a2800dbcc826bde56f3772cc0397a41860
last_modified_at: 2023-12-29
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/cupsaccept.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># cupsaccept

Aceita trabalhos enviados para um ou mais destinos.
NOTA: destino se refere a uma impressora ou uma classe de impressoras.
Veja também: `cupsreject`, `cupsenable`, `cupsdisable`, `lpstat`.
Mais informações: <https://openprinting.github.io/cups/doc/man-cupsaccept.html>.

- Aceita trabalhos de impressão para os destinos especificados:

`cupsaccept `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">destino1 destino2 ...</span>

- Especifica um servidor diferente:

`cupsaccept -h `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">server</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">destino1 destino2 ...</span>
