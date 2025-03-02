---
layout: page
title: common/stty (español)
description: "Establece opciones para una interfaz del dispositivo terminal."
content_hash: ec7437678c188be00ee138cfd9c1c235af20f929
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/stty.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/stty.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/stty.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/stty.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/stty.html
    icon: bi bi-globe
tldri18n_status: 2
---
# stty

Establece opciones para una interfaz del dispositivo terminal.
Más información: <https://www.gnu.org/software/coreutils/manual/html_node/stty-invocation.html>.

- Muestra todas las opciones de la terminal actual:

`stty --all`

- Establece el número de filas o columnas:

`stty `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filas|columnas</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cuenta</span>

- Obtiene la velocidad de transferencia real de un dispositivo:

`stty --file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo_del_dispositivo</span>` speed`

- Restablece todos los modos a valores razonables para el terminal actual:

`stty sane`

- Cambia entre modo raw y cooked:

`stty `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">raw|cooked</span>

- Desactiva o activa el eco de caracteres:

`stty `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-echo|echo</span>
