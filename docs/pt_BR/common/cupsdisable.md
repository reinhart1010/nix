---
layout: page
title: common/cupsdisable (português (Brasil))
description: "Para impressoras e classes."
content_hash: 3d7f07f2d46982b0dd946723ea66decaa32d6b15
last_modified_at: 2023-12-29
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/cupsdisable.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># cupsdisable

Para impressoras e classes.
NOTA: destino se refere a uma impressora ou uma classe de impressoras.
Veja também: `cupsenable`, `cupsaccept`, `cupsreject`, `lpstat`.
Mais informações: <https://openprinting.github.io/cups/doc/man-cupsenable.html>.

- Para um ou mais destino(s):

`cupsdisable `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">destino1 destino2 ...</span>

- Cancela todos os trabalhos do(s) destino(s) especificado(s):

`cupsdisable -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">destino1 destino2 ...</span>
