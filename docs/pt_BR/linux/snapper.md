---
layout: page
title: linux/snapper (português (Brasil))
description: "Ferramenta de gerenciamento de snapshots do sistema de arquivos."
content_hash: 6177388ff26bc922e376eaf8822941582095f8cc
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/linux/snapper.html
    icon: bi bi-globe
tldri18n_status: 2
---
# snapper

Ferramenta de gerenciamento de snapshots do sistema de arquivos.
Mais informações: <http://snapper.io/manpages/snapper.html>.

- Lista configurações de snapshots:

`snapper list-configs`

- Cria configuração do snapper:

`snapper -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">configuração</span>` create-config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/diretório</span>

- Cria um snapshot com uma descrição:

`snapper -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">configuração</span>` create -d "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">descrição_do_snapshot</span>`"`

- Lista snapshots para uma configuração:

`snapper -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">configuração</span>` list`

- Exclue um snapshot:

`snapper -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">configuração</span>` delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">número_do_snapshot</span>

- Exclue um intervalo de snapshots:

`snapper -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">configuração</span>` delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">snapshot_X</span>`-`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">snapshot_Y</span>
