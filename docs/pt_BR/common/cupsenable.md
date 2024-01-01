---
layout: page
title: common/cupsenable (português (Brasil))
description: "Inicia impressoras e classes."
content_hash: d8c307ba8ba6dd81206eda3d0e7d4d75c7f5b44f
last_modified_at: 2024-01-01
related_topics:
  - title: English version
    url: /en/common/cupsenable.html
    icon: bi bi-globe
tldri18n_status: 2
---
# cupsenable

Inicia impressoras e classes.
NOTA: destino se refere a uma impressora ou uma classe de impressoras.
Veja também: `cupsdisable`, `cupsaccept`, `cupsreject`, `lpstat`.
Mais informações: <https://www.cups.org/doc/man-cupsenable.html>.

- Inicia um ou mais destino(s):

`cupsenable `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">destino1 destino2 ...</span>

- Resume a impressão de trabalhos pendentes de um destino (use após `cupsdisable` com `--hold`):

`cupsenable --release `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">destination</span>

- Cancela todos os trabalhos do(s) destino(s) especificado(s):

`cupsenable -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">destination1 destination2 ...</span>
