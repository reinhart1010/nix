---
layout: page
title: linux/fdisk (português (Brasil))
description: "Gerenciador de tabelas de partições e partições no disco rígido."
content_hash: f605053e9ee2831c6e53b7afacaa0caa58031244
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/linux/fdisk.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/linux/fdisk.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/linux/fdisk.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># fdisk

Gerenciador de tabelas de partições e partições no disco rígido.
Mais informações: <https://manned.org/fdisk>.

- Exibir as partições:

`fdisk -l`

- Iniciar o manipulador de partições:

`fdisk `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sda</span>
