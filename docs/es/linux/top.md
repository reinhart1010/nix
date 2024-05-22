---
layout: page
title: linux/top (español)
description: "Muestra información dinámica en tiempo real sobre procesos ejecutándose."
content_hash: 955ae7a66d2441df01a602d4562f16c6c3c04874
last_modified_at: 2024-05-22
related_topics:
  - title: català version
    url: /ca/linux/top.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/top.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/top.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/linux/top.html
    icon: bi bi-globe
tldri18n_status: 2
---
# top

Muestra información dinámica en tiempo real sobre procesos ejecutándose.
Más información: <https://manned.org/top>.

- Inicia top:

`top`

- Oculta los procesos inactivos o zombies:

`top -i`

- Muestra solo procesos pertenecientes a un usuario dado:

`top -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">usuario</span>

- Ordena procesos por una columna:

`top -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_columna</span>

- Muestra los hilos individuales de un proceso dado:

`top -Hp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">identificador_de_proceso</span>

- Muestra solo los procesos con un(os) PID(s) dado(s), separados por comas. (Normalmente no se conoce el PID de antemano. Este ejemplo lo obtiene del nombre del proceso):

`top -p $(pgrep -d ',' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_proceso</span>`)`

- Obtén ayuda acerca de los comandos interactivos:

`?`
