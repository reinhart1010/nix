---
layout: page
title: linux/alien (português (Brasil))
description: "Converter diferentes pacotes de instalação para outros formatos."
content_hash: f614d80e0845e7f5b6164a8eb6494ed55acee59c
last_modified_at: 2023-12-28
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

- Converte um arquivo de instalação específico para o formato Debian (extensão `.deb`):

`sudo alien --to-deb `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo</span>

- Converte um arquivo de instalação específico para o formato Red Hat (extensão `.rpm`):

`sudo alien --to-rpm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo</span>

- Converte um arquivo de instalação específico para um arquivo de instalação do Slackware (extensão `.tgz`):

`sudo alien --to-tgz `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo</span>

- Converte um arquivo de instalação específico para o formato Debian e instala no sistema:

`sudo alien --to-deb --install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo</span>
