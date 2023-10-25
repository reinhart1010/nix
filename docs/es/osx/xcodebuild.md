---
layout: page
title: osx/xcodebuild (español)
description: "Construye proyectos Xcode."
content_hash: 72071b8d4157a6b14bf26d425672b72294261cf9
last_modified_at: 2023-10-25
related_topics:
  - title: English version
    url: /en/osx/xcodebuild.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/xcodebuild.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># xcodebuild

Construye proyectos Xcode.
Más información: <https://developer.apple.com/library/archive/technotes/tn2339/_index.html>.

- Construye espacio de trabajo:

`xcodebuild -workspace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_del_espacio_de_trabajo.workspace</span>` -scheme `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_scheme</span>` -configuration `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_configuration</span>` clean build SYMROOT=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta_SYMROOT</span>

- Construye proyecto:

`xcodebuild -target `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_target</span>` -configuration `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_configuration</span>` clean build SYMROOT=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta_SYMROOT</span>

- Muestra los SDKs:

`xcodebuild -showsdks`
