---
layout: page
title: common/lpoptions (português (Brasil))
description: "Exibe ou define opções e padrões de uma impressora."
content_hash: 4a8a43d8ae96fd9252ae97905df73ca985f0bf5f
last_modified_at: 2023-12-28
related_topics:
  - title: English version
    url: /en/common/lpoptions.html
    icon: bi bi-globe
tldri18n_status: 2
---
# lpoptions

Exibe ou define opções e padrões de uma impressora.
Veja também: `lpadmin`.
Mais informações: <https://openprinting.github.io/cups/doc/man-lpoptions.html>.

- Define a impressora padrão:

`lpoptions -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">impressora[/instância]</span>

- Lista opções específicas de uma impressora:

`lpoptions -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">impressora</span>` -l`

- Define uma nova opção em uma impressora:

`lpoptions -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">impressora</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">opção[=valor]</span>

- Exclui as opções de uma impressora específica:

`lpoptions -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">impressora</span>` -x`
