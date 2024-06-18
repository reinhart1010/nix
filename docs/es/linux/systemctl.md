---
layout: page
title: linux/systemctl (español)
description: "Controla el gestor de sistemas y servicios systemd."
content_hash: 953c364735d4cda1737839ebf0e785570a1e7708
last_modified_at: 2024-06-18
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

Controla el gestor de sistemas y servicios systemd.
Más información: <https://www.freedesktop.org/software/systemd/man/systemctl.html>.

- Muestra todos los servicios en ejecución:

`systemctl status`

- Lista las unidades fallidas:

`systemctl --failed`

- Inicia, para, reinicia, recarga o muestra el estado de una unidad:

`systemctl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">start|stop|restart|reload|status</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">unidad</span>

- Habilita o deshabilita una unidad para iniciarla al arrancar:

`systemctl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">enable|disable</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">unidad</span>

- Reinicia systemd, lee unidades nuevas o modificadas:

`systemctl daemon-reload`

- Checa si una unidad está activa, habilitada, o en estado fallido:

`systemctl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">is-active|is-enabled|is-failed</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">unidad</span>

- Lista todos los servicios, sockets, unidades auto-montadas filtradas por estado en ejecución o fallido:

`systemctl list-units --type=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">service|socket|automount</span>` --state=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">failed|running</span>

- Muestra los contenidos y la ruta absoluta del archivo de una unidad:

`systemctl cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">unidad</span>
