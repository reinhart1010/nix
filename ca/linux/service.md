---
layout: page
title: linux/service (català)
description: "Gestiona els serveis mitjançant l'execució de scripts init."
content_hash: 82008bbd970251086df69eae7f835ac9b231a6a9
related_topics:
  - title: English version
    url: /en/linux/service.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/service.html
    icon: bi bi-globe
---
# service

Gestiona els serveis mitjançant l'execució de scripts init.
S'ha d'ometre la ruta completa del script (s'assumeix `/etc/init.d`).

- Llista el nom i l'estat de tots els serveis:

`service --status-all`

- Inicia/Para/Reinicia/Recarrega servei (_start_/_stop_ hauria d'estar sempre disponible):

`service `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_del_servei</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">start|stop|restart|reload</span>

- Fa un reinici complet (executa el script dues vegades amb _start_ i _stop_):

`service `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_del_servei</span>` --full-restart`

- Mostra l'estat actual d'un servei:

`service `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_del_servei</span>` status`
