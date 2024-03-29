---
layout: page
title: osx/pod (español)
description: "Gestor de dependencias para proyectos Swift y Objective-C Cocoa."
content_hash: e7d76693a5bb044341edf67caabd04e74de0cba0
last_modified_at: 2023-11-26
related_topics:
  - title: English version
    url: /en/osx/pod.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/pod.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pod

Gestor de dependencias para proyectos Swift y Objective-C Cocoa.
Más información: <https://guides.cocoapods.org/terminal/commands.html>.

- Crea un Podfile para el proyecto actual con los contenidos por defecto:

`pod init`

- Descarga e instala todos los pods definidos en el Podfile (que no hayan sido instalados antes):

`pod install`

- Lista todos los pods disponibles:

`pod list`

- Muestra los pods obsoletos (de los instalados actualmente):

`pod outdated`

- Actualiza todos los pods instalados a su versión más reciente:

`pod update`

- Actualiza un pod específico (previamente instalado) a su versión más reciente:

`pod update `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_del_pod</span>

- Elimina CocoaPods de un proyecto Xcode:

`pod deintegrate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">proyecto_xcode</span>
