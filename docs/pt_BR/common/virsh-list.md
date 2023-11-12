---
layout: page
title: common/virsh-list (português (Brasil))
description: "Liste o ID, nome e estado das máquinas virtuais."
content_hash: 613d05a44252727b47bc41bc22753e1da05dca0d
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/virsh-list.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/virsh-list.html
    icon: bi bi-globe
tldri18n_status: 2
---
# virsh-list

Liste o ID, nome e estado das máquinas virtuais.
Veja também: `virsh`.
Mais informações: <https://manned.org/virsh>.

- Listar informações sobre máquinas virtuais em execução:

`virsh list`

- Listar informações sobre máquinas virtuais independentemente do estado:

`virsh list --all`

- Listar informações sobre máquinas virtuais com autostart ativado ou desativado:

`virsh list --all --`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">autostart|no-autostart</span>

- Listar informações sobre máquinas virtuais com ou sem snapshots:

`virsh list --all --`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">with-snapshot|without-snapshot</span>
