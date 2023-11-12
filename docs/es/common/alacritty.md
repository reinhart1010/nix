---
layout: page
title: common/alacritty (español)
description: "Emulador de terminal acelerado por GPU y multiplataforma."
content_hash: c8e7ac528dc17cb53a2c7a925794c54379ce1034
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/alacritty.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/alacritty.html
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
  - title: português (Portugal) version
    url: /pt_PT/common/alacritty.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/alacritty.html
    icon: bi bi-globe
tldri18n_status: 2
---
# alacritty

Emulador de terminal acelerado por GPU y multiplataforma.
Más información: <https://github.com/alacritty/alacritty>.

- Abre una nueva ventana de Alacritty:

`alacritty`

- Ejecuta Alacritty en un directorio específico:

`alacritty --working-directory `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/directorio</span>

- Ejecuta un comando en una nueva ventana de Alacritty:

`alacritty -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>

- Especifica un archivo de configuración alternativo (por defecto es `$XDG_CONFIG_HOME/alacritty/alacritty.yml`):

`alacritty --config-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/config.yml</span>

- Ejecuta con recarga automática de la configuración activada (puede activarse por defecto en `alacritty.yml`):

`alacritty --live-config-reload --config-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/config.yml</span>
