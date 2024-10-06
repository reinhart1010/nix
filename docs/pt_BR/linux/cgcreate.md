---
layout: page
title: linux/cgcreate (português (Brasil))
description: "Cria cgroups, usados para limitar, medir e controlar recursos usados pelos processos."
content_hash: 8d0b4cd9d2e76ec1cb2f205173f774c43e2768d6
last_modified_at: 2024-10-06
related_topics:
  - title: English version
    url: /en/linux/cgcreate.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/cgcreate.html
    icon: bi bi-globe
tldri18n_status: 2
---
# cgcreate

Cria cgroups, usados para limitar, medir e controlar recursos usados pelos processos.
Tipos de `cgroups` podem ser `memory`, `cpu`, `net_cls`, etc.
Mais informações: <https://manned.org/cgcreate>.

- Cria um novo grupo:

`cgcreate -g `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tipo_grupo</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_grupo</span>

- Cria um novo grupo com vários tipos de cgroup:

`cgcreate -g `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tipo_grupo1</span>`,`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tipo_grupo2</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_grupo</span>

- Cria um subgrupo:

`mkdir /sys/fs/cgroup/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tipo_grupo2</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_grupo</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_subgrupo</span>
