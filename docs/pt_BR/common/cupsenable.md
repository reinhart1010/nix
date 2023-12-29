---
layout: page
title: common/cupsenable (português (Brasil))
description: "Inicia impressoras e classes."
content_hash: 7138e34431402fd8eab714a415511da0e1efc183
last_modified_at: 2023-12-29
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/cupsenable.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># cupsenable

Inicia impressoras e classes.
NOTA: destino se refere a uma impressora ou uma classe de impressoras.
Veja também: `cupsdisable`, `cupsaccept`, `cupsreject`, `lpstat`.
Mais informações: <https://openprinting.github.io/cups/doc/man-cupsenable.html>.

- Inicia um ou mais destino(s):

`cupsenable `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">destino1 destino2 ...</span>

- Resume a impressão de trabalhos pendentes de um destino (use após `cupsdisable` com `--hold`):

`cupsenable --release `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">destination</span>

- Cancela todos os trabalhos do(s) destino(s) especificado(s):

`cupsenable -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">destination1 destination2 ...</span>
