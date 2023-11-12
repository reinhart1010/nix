---
layout: page
title: linux/systemctl (español)
description: "Controla el sistema systemd y el gestor de servicios."
content_hash: 40c4ae3a7f97de2c2af103429b21b34d1389d021
last_modified_at: 2023-11-12
related_topics:
  - title: català version
    url: /ca/linux/systemctl.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/systemctl.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/systemctl.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/linux/systemctl.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/systemctl.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/systemctl.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/systemctl.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/linux/systemctl.html
    icon: bi bi-globe
tldri18n_status: 2
---
# systemctl

Controla el sistema systemd y el gestor de servicios.
Más información: <https://www.freedesktop.org/software/systemd/man/systemctl.html>.

- Muestra todos los servicios en ejecución:

`systemctl status`

- Lista las unidades fallidas:

`systemctl --failed`

- Inicia/Para/Reinicia/Recarga un servicio:

`systemctl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">start|stop|restart|reload</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">unidad</span>

- Muestra el estado de una unidad:

`systemctl status `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">unidad</span>

- Habilita/Deshabilita una unidad para que se inicie en el arranque:

`systemctl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">enable/disable</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">unidad</span>

- Enmascara/Desenmascara una unidad para evitar su habilitación y activación manual:

`systemctl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mask|unmask</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">unidad</span>

- Recarga systemd, buscando unidades nuevas o modificadas:

`systemctl daemon-reload`

- Comprueba si una unidad está habilitada:

`systemctl is-enabled `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">unidad</span>
