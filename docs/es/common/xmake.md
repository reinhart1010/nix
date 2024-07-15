---
layout: page
title: common/xmake (español)
description: "Una utilidad de compilación multiplataforma C & C++ basada en Lua."
content_hash: 5c9b20e69a8385b0217af1f9198f991cba55aeab
last_modified_at: 2024-07-15
related_topics:
  - title: English version
    url: /en/common/xmake.html
    icon: bi bi-globe
tldri18n_status: 2
---
# xmake

Una utilidad de compilación multiplataforma C & C++ basada en Lua.
Más información: <https://xmake.io/#/getting_started>.

- Crea un proyecto Xmake C, consistente en un hello world y `xmake.lua`:

`xmake create --language c -P `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_del_proyecto</span>

- Construye y ejecuta un proyecto Xmake:

`xmake build run`

- Ejecuta directamente un objetivo Xmake compilado:

`xmake run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_del_objetivo</span>

- Configura los objetivos de compilación de un proyecto:

`xmake config --plat=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">macosx|linux|iphoneos|...</span>` --arch=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">x86_64|i386|arm64| ..</span>` --mode=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">debug|release</span>

- Instala el objetivo compilado en un directorio:

`xmake install -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/directorio</span>
