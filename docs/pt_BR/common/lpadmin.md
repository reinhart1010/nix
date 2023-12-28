---
layout: page
title: common/lpadmin (português (Brasil))
description: "Configura impressoras e classes do CUPS."
content_hash: f404ba435443663ac9b9a142a8ee3bb6b5798539
last_modified_at: 2023-12-28
related_topics:
  - title: English version
    url: /en/common/lpadmin.html
    icon: bi bi-globe
tldri18n_status: 2
---
# lpadmin

Configura impressoras e classes do CUPS.
Veja também: `lpoptions`.
Mais informações: <https://openprinting.github.io/cups/doc/man-lpadmin.html>.

- Define a impressora padrão:

`lpadmin -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">impressora</span>

- Exclui uma impressora ou classe específica:

`lpadmin -x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">impressora|classe</span>

- Adiciona uma impressora a uma classe:

`lpadmin -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">impressora</span>` -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">classe</span>

- Remove uma impressora de uma classe:

`lpadmin -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">impressora</span>` -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">classe</span>
