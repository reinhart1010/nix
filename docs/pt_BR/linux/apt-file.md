---
layout: page
title: linux/apt-file (português (Brasil))
description: "Buscador de arquivos nos pacotes APT, incluindo os não instalados."
content_hash: 0b54211ae47913321b297484cefa8fa633f5cc30
last_modified_at: 2024-03-14
related_topics:
  - title: català version
    url: /ca/linux/apt-file.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/linux/apt-file.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/apt-file.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/apt-file.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/apt-file.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/linux/apt-file.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/apt-file.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/apt-file.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/apt-file.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># apt-file

Buscador de arquivos nos pacotes APT, incluindo os não instalados.
Mais informações: <https://manpages.debian.org/latest/apt-file/apt-file.1.html>.

- Atualiza as informações dos pacotes a partir de todos os repositórios remotos:

`sudo apt update`

- Busca por pacotes que contêm o arquivo ou caminho especificado:

`apt-file search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_pacote_ou_caminho</span>

- Lista o conteúdo de um pacote específico:

`apt-file list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_pacote</span>
