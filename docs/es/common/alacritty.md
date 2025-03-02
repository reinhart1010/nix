---
layout: page
title: common/alacritty (español)
description: "Emulador de terminal multiplataforma acelerado por GPU."
content_hash: b7adf65f0e9548eea31973d02601b42203fbb7d4
last_modified_at: 2025-03-02
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

Emulador de terminal multiplataforma acelerado por GPU.
Más información: <https://github.com/alacritty/alacritty>.

- Inicia un nuevo proceso Alacritty y crea una ventana:

`alacritty`

- Inicia el programa residente de Alacritty (sin crear una ventana):

`alacritty --daemon`

- Crea una nueva ventana utilizando el proceso Alacritty que ya está en marcha:

`alacritty msg create-window`

- Inicia el intérprete de comandos en un directorio específico (también funciona con `alacritty msg create-window`):

`alacritty --working-directory `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/directorio</span>

- [e]jecuta un comando en una nueva ventana de Alacritty (también funciona con `alacritty msg create-window`):

`alacritty -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>

- Utiliza un archivo de configuración alternativo (por defecto es `$XDG_CONFIG_HOME/alacritty/alacritty.toml`):

`alacritty --config-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/config.toml</span>

- Ejecuta con la recarga de la configuración activa (también puede activarse por defecto en `alacritty.toml`):

`alacritty --live-config-reload --config-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/config.toml</span>
