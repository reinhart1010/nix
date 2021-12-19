---
layout: page
title: linux/apt-mark (português (Brasil))
description: "Utilitário que altera as configurações dos pacotes instalados."
content_hash: 4573e72af68b8b30de225d8bd4356743775f44a9
related_topics:
  - title: Deutsch version
    url: /de/linux/apt-mark.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/apt-mark.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/apt-mark.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/apt-mark.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/apt-mark.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/apt-mark.html
    icon: bi bi-globe
---
# apt-mark

Utilitário que altera as configurações dos pacotes instalados.
Mais informações: <https://manpages.debian.org/latest/apt/apt-mark.8.html>.

- Marcar um pacote como instalado automaticamente:

`sudo apt-mark auto `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_pacote</span>

- Bloquear um pacote na sua versão atual, impedindo que ele seja atualizado:

`sudo apt-mark hold `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_pacote</span>

- Desbloquear um pacote, permitindo que ele seja atualizado:

`sudo apt-mark unhold `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_pacote</span>

- Listar os pacotes instalados manualmente:

`apt-mark showmanual`

- Listar os pacotes bloqueados:

`apt-mark showhold`
