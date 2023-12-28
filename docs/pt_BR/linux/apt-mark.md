---
layout: page
title: linux/apt-mark (português (Brasil))
description: "Utilitário que altera as configurações dos pacotes instalados."
content_hash: b341f356a153fece0c9a2493c9e190ce600ab333
last_modified_at: 2023-12-28
related_topics:
  - title: català version
    url: /ca/linux/apt-mark.html
    icon: bi bi-globe
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
  - title: polski version
    url: /pl/linux/apt-mark.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/apt-mark.html
    icon: bi bi-globe
tldri18n_status: 2
---
# apt-mark

Utilitário que altera as configurações dos pacotes instalados.
Mais informações: <https://manpages.debian.org/latest/apt/apt-mark.8.html>.

- Marca um pacote como instalado automaticamente:

`sudo apt-mark auto `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_pacote</span>

- Bloqueia um pacote na sua versão atual, impedindo que ele seja atualizado:

`sudo apt-mark hold `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_pacote</span>

- Desbloqueia um pacote, permitindo que ele seja atualizado:

`sudo apt-mark unhold `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_pacote</span>

- Lista os pacotes instalados manualmente:

`apt-mark showmanual`

- Lista os pacotes bloqueados:

`apt-mark showhold`
