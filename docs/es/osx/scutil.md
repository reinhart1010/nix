---
layout: page
title: osx/scutil (español)
description: "Gestiona los parámetros de configuración del sistema."
content_hash: 1f3151fc9efc26177450cacbc29222f0a763a785
last_modified_at: 2024-01-31
related_topics:
  - title: English version
    url: /en/osx/scutil.html
    icon: bi bi-globe
  - title: português (Portugal) version
    url: /pt_PT/osx/scutil.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/scutil.html
    icon: bi bi-globe
tldri18n_status: 2
---
# scutil

Gestiona los parámetros de configuración del sistema.
Es necesario ser root para establecer la configuración.
Más información: <https://keith.github.io/xcode-man-pages/scutil.8.html>.

- Muestra la configuración DNS:

`scutil --dns`

- Muestra la configuración del proxy:

`scutil --proxy`

- Obtén el nombre del equipo:

`scutil --get ComputerName`

- Establece el nombre del equipo:

`sudo scutil --set ComputerName `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_ordenador</span>

- Obtén el nombre del host:

`scutil --get HostName`

- Establece nombre del host:

`scutil --set HostName `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_host</span>
