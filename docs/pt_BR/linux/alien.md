---
layout: page
title: linux/alien (português (Brasil))
description: "Converter diferentes pacotes de instalação para outros formatos."
content_hash: e448a1fe5644ad066f02ea0fd4559d7f5e020262
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/linux/alien.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/alien.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/alien.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/alien.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/linux/alien.html
    icon: bi bi-globe
tldri18n_status: 2
---
# alien

Converter diferentes pacotes de instalação para outros formatos.
Mais informações: <https://manned.org/alien>.

- Converter um arquivo de instalação específico para o formato Debian (extensão `.deb`):

`sudo alien --to-deb `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo</span>

- Converter um arquivo de instalação específico para o formato Red Hat (extensão `.rpm`):

`sudo alien --to-rpm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo</span>

- Converter um arquivo de instalação específico para um arquivo de instalação do Slackware (extensão `.tgz`):

`sudo alien --to-tgz `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo</span>

- Converter um arquivo de instalação específico para o formato Debian e instalar no sistema:

`sudo alien --to-deb --install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo</span>
