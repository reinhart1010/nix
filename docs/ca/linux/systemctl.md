---
layout: page
title: linux/systemctl (català)
description: "Controla el sistema systemd i el gestor de serveis."
content_hash: ff8b6254779a04f3f11a555fb9e99f548ff15bf6
last_modified_at: 2023-12-28
related_topics:
  - title: English version
    url: /en/linux/systemctl.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/systemctl.html
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

Controla el sistema systemd i el gestor de serveis.
Més informació: <https://www.freedesktop.org/software/systemd/man/systemctl.html>.

- Mostra tots els serveis en execució:

`systemctl status`

- Llista les unitats fallides:

`systemctl --failed`

- Inicia/Atura/Reinicia/Recarrega un servei:

`systemctl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">start|stop|restart|reload</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">unitat</span>

- Mostra l'estat d'una unitat:

`systemctl status `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">unitat</span>

- Habilita/Deshabilita una unitat perquè s'inicii en l'arrencada:

`systemctl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">enable|disable</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">unitat</span>

- Enmascara/Desenmascara una unitat per evitar la seva habilitació i activació manual:

`systemctl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mask|unmask</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">unida</span>

- Recarrega systemd, buscant unitats noves o modificades:

`systemctl daemon-reload`

- Comprova si una unitat està habilitada:

`systemctl is-enabled `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">unitat</span>
