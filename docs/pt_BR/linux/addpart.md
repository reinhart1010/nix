---
layout: page
title: linux/addpart (português (Brasil))
description: "Informa ao kernel do Linux sobre a existência da partição especificada."
content_hash: fcdbd03cd9c2caa63692647190ea2c0ba0b2f464
last_modified_at: 2023-12-28
related_topics:
  - title: català version
    url: /ca/linux/addpart.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/linux/addpart.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/addpart.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/addpart.html
    icon: bi bi-globe
tldri18n_status: 2
---
# addpart

Informa ao kernel do Linux sobre a existência da partição especificada.
O comando é um wrapper do ioctl `add partition`.
Mais informações: <https://manned.org/addpart>.

- Informa ao kernel do Linux sobre a existência da partição especificada:

`addpart `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dispositivo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">particao</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">inicio</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tamanho</span>
