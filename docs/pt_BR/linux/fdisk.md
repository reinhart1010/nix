---
layout: page
title: linux/fdisk (português (Brasil))
description: "Gerenciador de tabelas de partições e partições no disco rígido."
content_hash: f605053e9ee2831c6e53b7afacaa0caa58031244
related_topics:
  - title: English version
    url: /en/linux/fdisk.html
    icon: bi bi-globe
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/fdisk.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># fdisk

Gerenciador de tabelas de partições e partições no disco rígido.
Mais informações: <https://manned.org/fdisk>.

- Exibir as partições:

`fdisk -l`

- Iniciar o manipulador de partições:

`fdisk `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sda</span>
