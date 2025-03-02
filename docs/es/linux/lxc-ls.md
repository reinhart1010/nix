---
layout: page
title: linux/lxc-ls (español)
description: "Lista contenedores Linux."
content_hash: 0ee52ad406084467cfe2743f5bd2e4fb90fdeb73
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/linux/lxc-ls.html
    icon: bi bi-globe
tldri18n_status: 2
---
# lxc-ls

Lista contenedores Linux.
Más información: <https://linuxcontainers.org/lxc/manpages/man1/lxc-ls.1.html>.

- Lista contenedores activos (incluyendo congelados y en ejecución):

`lxc-ls --active`

- Lista solo contenedores congelados:

`lxc-ls --frozen`

- Lista solo contenedores parados:

`lxc-ls --stopped`

- Lista contenedores en una salida elegante, basada en columnas:

`lxc-ls --fancy`
