---
layout: page
title: linux/shutdown (italiano)
description: "Spegni e riavvia il sistema."
content_hash: 2be464563bfb7587c3baee63ce1284186b0139b8
related_topics:
  - title: English version
    url: /en/linux/shutdown.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/shutdown.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/shutdown.html
    icon: bi bi-globe
---
# shutdown

Spegni e riavvia il sistema.
Maggiori informazioni: <https://manned.org/shutdown.8>.

- Spegni il sistema immediatamente:

`shutdown -h now`

- Riavvia il sistema immediatamente:

`shutdown -r now`

- Riavvia il sistema in 5 minuti:

`shutdown -r +`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>` &`

- Spegni il sistema alle 13:

`shutdown -h 13:00`

- Annulla un'operazione programmata di riavvio o spegnimento:

`shutdown -c`
