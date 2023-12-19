---
layout: page
title: linux/conky (español)
description: "Monitor de sistema ligero para X."
content_hash: 3d33b42784e0cf0e649619149e702c1842ea3547
last_modified_at: 2023-12-19
related_topics:
  - title: català version
    url: /ca/linux/conky.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/conky.html
    icon: bi bi-globe
tldri18n_status: 2
---
# conky

Monitor de sistema ligero para X.
Más información: <https://github.com/brndnmtthws/conky>.

- Ejecuta con la configuración por defecto:

`conky`

- Crea una nueva configuración por defecto:

`conky -C > ~/.conkyrc`

- Ejecuta conky con un archivo de configuración concreto:

`conky -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/la/configuración</span>

- Ejecuta en segundo plano (daemon):

`conky -d`

- Alinea conky en el escritorio:

`conky -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">top|bottom|middle</span>`_`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">left|right|middle</span>

- Pausa de 5 segundos al iniciar antes de ejecutarlo:

`conky -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>
