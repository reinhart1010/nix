---
layout: page
title: linux/apt-file (português (Brasil))
description: "Buscador de arquivos nos pacotes apt, incluindo os não instalados."
content_hash: 1e6bf92735d20b38978fb3c03ae075d910bab7d2
related_topics:
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
  - title: italiano version
    url: /it/linux/apt-file.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/apt-file.html
    icon: bi bi-globe
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/apt-file.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># apt-file

Buscador de arquivos nos pacotes apt, incluindo os não instalados.
Mais informações: <https://manpages.debian.org/latest/apt-file/apt-file.1.html>.

- Atualizar as informações dos pacotes a partir de todos os repositórios remotos:

`sudo apt update`

- Buscar por pacotes que contêm o arquivo ou caminho especificado:

`apt-file search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_pacote_ou_caminho</span>

- Listar o conteúdo de um pacote específico:

`apt-file list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_pacote</span>
