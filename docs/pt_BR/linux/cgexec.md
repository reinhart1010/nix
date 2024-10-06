---
layout: page
title: linux/cgexec (português (Brasil))
description: "Limita, mede e controla recursos usados pelos processos."
content_hash: a7f1e4640cc73a1671220eaa0b82837ec27f8676
last_modified_at: 2024-10-06
related_topics:
  - title: English version
    url: /en/linux/cgexec.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/cgexec.html
    icon: bi bi-globe
tldri18n_status: 2
---
# cgexec

Limita, mede e controla recursos usados pelos processos.
Há vários tipos de cgroup (conhecidos como controladores), tal como `cpu`, `memory`, etc.
Mais informações: <https://manned.org/cgexec>.

- Executa um processo em um cgroup e controlador providos pelo usuário:

`cgexec -g `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">controlador</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_cgroup</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_processo</span>
