---
layout: page
title: common/alacritty (português (Portugal))
description: "Emulador de terminal multiplataforma acelerado por GPU."
content_hash: d10ecbf166f9979fc3bac843b21231ac9336989d
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
  - title: português (Brasil) version
    url: /pt_BR/common/alacritty.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/alacritty.html
    icon: bi bi-globe
tldri18n_status: 2
---
# alacritty

Emulador de terminal multiplataforma acelerado por GPU.
Mais informações: <https://github.com/alacritty/alacritty>.

- Abrir Alacritty numa nova janela:

`alacritty`

- Executar na directoria especificada:

`alacritty --working-directory `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/directoria</span>

- Executar commando numa nova janela de Alacritty:

`alacritty -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>

- Definir caminho alternativo para o ficheiro de configuração (por omissão `$XDG_CONFIG_HOME/alacritty/alacritty.yml`):

`alacritty --config-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/configuração.yml</span>

- Executar com carregamento automático de configuração (pode ser definido por omissão em `alacritty.yml`):

`alacritty --live-config-reload --config-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/configuração.yml</span>
