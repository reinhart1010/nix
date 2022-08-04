---
layout: page
title: linux/systemctl (català)
description: "Controla el sistema systemd i el gestor de serveis."
content_hash: 769cabeffe001014915b2f5c7187502950312fd6
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

`systemctl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mask|unmask</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">unida`

- Recarrega systemd, buscant unitats noves o modificades:

`systemctl daemon-reload`

- Comprova si una unitat està habilitada:

`systemctl is-enabled `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">unitat</span>
