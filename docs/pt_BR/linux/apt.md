---
layout: page
title: linux/apt (português (Brasil))
description: "Utilitário de gerenciamento de pacotes de distribuições baseadas em Debian."
content_hash: e45bb42294cba33960af369a84489f28bd006c3b
last_modified_at: 2024-10-02
related_topics:
  - title: العربية version
    url: /ar/linux/apt.html
    icon: bi bi-globe
  - title: বাংলা version
    url: /bn/linux/apt.html
    icon: bi bi-globe
  - title: català version
    url: /ca/linux/apt.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/linux/apt.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/apt.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/apt.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/apt.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/linux/apt.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/linux/apt.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/apt.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/linux/apt.html
    icon: bi bi-globe
  - title: മലയാളം version
    url: /ml/linux/apt.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/apt.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/apt.html
    icon: bi bi-globe
  - title: português (Portugal) version
    url: /pt_PT/linux/apt.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/linux/apt.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/apt.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/linux/apt.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/apt.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># apt

Utilitário de gerenciamento de pacotes de distribuições baseadas em Debian.
Substituto recomendado para `apt-get` quando usado de forma interativa em versões do Ubuntu mais novas que 16.04.
Para comandos equivalentes em outros gerenciadores de pacotes, veja <https://wiki.archlinux.org/title/Pacman/Rosetta>.
Mais informações: <https://manned.org/apt.8>.

- Atualiza a lista de pacotes e versões disponíveis (recomenda-se executá-lo antes de outros comandos `apt`):

`sudo apt update`

- Busca por um determinado pacote:

`apt search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pacote</span>

- Exibe as informações de um pacote:

`apt show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pacote</span>

- Instala um pacote ou atualiza-o para a versão mais recente:

`sudo apt install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pacote</span>

- Remove um pacote (para remover também os arquivos de configuração deve-se usar a opção `purge` ao invés do `remove`):

`sudo apt remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pacote</span>

- Atualiza todos os pacotes instalados para suas versões mais recentes:

`sudo apt upgrade`

- Lista todos os pacotes:

`apt list`

- Lista todos os pacotes instalados:

`apt list --installed`
