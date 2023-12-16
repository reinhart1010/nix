---
layout: page
title: windows/nvm (español)
description: "Instala, desinstala o cambia entre versiones de Node.js."
content_hash: 5ad66552dabb4556494b74b3d772040dacd43a3c
last_modified_at: 2023-12-16
related_topics:
  - title: English version
    url: /en/windows/nvm.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/windows/nvm.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/windows/nvm.html
    icon: bi bi-globe
tldri18n_status: 2
---
# nvm

Instala, desinstala o cambia entre versiones de Node.js.
Admite números de versión como "12.8" o "v16.13.1", y etiquetas como "stable", "system", etc.
Más información: <https://github.com/coreybutler/nvm-windows>.

- Instala una versión específica de Node.js:

`nvm install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">versión_de_node</span>

- Establece la versión por defecto de Node.js (debe ejecutarse como Administrador):

`nvm use `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">versión_de_node</span>

- Lista todas las versiones disponibles de Node.js y destaca la versión por defecto:

`nvm list`

- Lista todas las versiones remotas de Node.js:

`nvm ls-remote`

- Desinstalación de una versión determinada de Node.js:

`nvm uninstall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">versión_de_node</span>
