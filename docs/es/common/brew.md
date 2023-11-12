---
layout: page
title: common/brew (español)
description: "Administrador de paquetes para macOS y Linux."
content_hash: 6e2f72e12ef99d1bccff08a1bc75e304a1260aab
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/brew.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/brew.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/brew.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/brew.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/brew.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/brew.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/brew.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/common/brew.html
    icon: bi bi-globe
tldri18n_status: 2
---
# brew

Administrador de paquetes para macOS y Linux.
Más información: <https://docs.brew.sh/Manpage>.

- Instala la última versión estable de una fórmula (usar `--devel` para versiones de desarrollo):

`brew install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">formula</span>

- Lista todas las fórmulas y casks instaladas:

`brew list`

- Actualiza una fórmula o cask instalada (si no se indica ninguna, todas las fórmulas/casks se actualizan):

`brew upgrade `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">formula</span>

- Trae la versión más reciente de Homebrew y todas sus fórmulas y casks desde el repositorio fuente de Homebrew:

`brew update`

- Muestra las fórmulas y casks que tienen una versión más reciente disponible:

`brew outdated`

- Busca fórmulas (por ej. paquetes) y casks (por ej. paquetes nativos) disponibles:

`brew search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">texto</span>

- Muestra la información de una fórmula o un cask (versión, ruta de instalación, dependencias, etc.):

`brew info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">formula</span>

- Revisa la instalación local de Homebrew en busca de problemas potenciales:

`brew doctor`
