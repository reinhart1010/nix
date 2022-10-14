---
layout: page
title: common/flips (português (Brasil))
description: "Cria e aplica patches em arquivos IPS e BPS."
content_hash: bb7376772287b9c34567b6ede5ced61bec7d31c6
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># flips

Cria e aplica patches em arquivos IPS e BPS.
Mais informações: <https://github.com/Alcaro/Flips>.

- Abre Flips para criar e aplicar um patch:

`flips`

- Aplica um patch criando um novo arquivo ROM:

`flips --apply `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">patch.bps</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rom.smc</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hack.smc</span>

- Cria um patch a partir de duas ROMs:

`flips --create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rom.smc</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hack.smc</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">patch.bps</span>
