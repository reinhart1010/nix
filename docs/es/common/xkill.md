---
layout: page
title: common/xkill (español)
description: "Cierra de manera forzosa una ventana interactivamente en una sesión gráfica."
content_hash: 87ba5e0a67ee4e4b8f77d397ab344c737f1338f7
last_modified_at: 2024-05-02
related_topics:
  - title: English version
    url: /en/common/xkill.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/xkill.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/xkill.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/xkill.html
    icon: bi bi-globe
  - title: português (Portugal) version
    url: /pt_PT/common/xkill.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># xkill

Cierra de manera forzosa una ventana interactivamente en una sesión gráfica.
Vea también `kill` y `killall`.
Más información: <https://www.x.org/releases/current/doc/man/man1/xkill.1.xhtml>.

- Muestra un cursor para cerrar forzosamente una ventana presionando con el botón izquierdo (presiona cualquier otro botón del ratón para cancelar):

`xkill`

- Muestra un cursor para seleccionar una ventana para cerrarla forzosamente al presionar cualquier botón del ratón:

`xkill -button any`

- Cierra forzosamente una ventana con un ID específico (use `xwininfo` para obtener información acerca de las ventanas):

`xkill -id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id</span>
