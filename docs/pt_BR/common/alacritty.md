---
layout: page
title: common/alacritty (português (Brasil))
description: "Terminal multiplataforma, acelerado por GPU."
content_hash: 442e0c7e191ebb718cf1ffc052eac8a7255d0ace
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/alacritty.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/alacritty.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/alacritty.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/alacritty.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/alacritty.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/alacritty.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/alacritty.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/alacritty.html
    icon: bi bi-globe
  - title: português (Portugal) version
    url: /pt_PT/common/alacritty.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/alacritty.html
    icon: bi bi-globe
tldri18n_status: 2
---
# alacritty

Terminal multiplataforma, acelerado por GPU.
Mais informações: <https://github.com/alacritty/alacritty>.

- Abre uma nova janela do Alacritty:

`alacritty`

- Roda em um diretório específico:

`alacritty --working-directory `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/diretório</span>

- Roda um comando em uma nova janela do Alacritty:

`alacritty -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>

- Especifica um arquivo de configuração alternativo (`$XDG_CONFIG_HOME/alacritty/alacritty.yml` por padrão):

`alacritty --config-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/config.yml</span>

- Executa com configuração ao vivo habilitada (pode também ser habilitada por padrão no `alacritty.yml`):

`alacritty --live-config-reload --config-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/config.yml</span>
