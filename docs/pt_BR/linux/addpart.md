---
layout: page
title: linux/addpart (português (Brasil))
description: "Informa ao kernel do Linux sobre a existência da partição especificada."
content_hash: 1aa9be79aaeae75c4098bbd9bfe7e08d33584986
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
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># addpart

Informa ao kernel do Linux sobre a existência da partição especificada.
O comando é um wrapper do ioctl `add partition`.
Mais informações: <https://manned.org/addpart>.

- Informar ao kernel do Linux sobre a existência da partição especificada:

`addpart `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dispositivo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">particao</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">inicio</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tamanho</span>
