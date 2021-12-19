---
layout: page
title: linux/nmtui (italiano)
description: "Interfaccia utente solo testo per NetworkManager."
content_hash: 4bd41b0144b10a9703c7cc556ca967445803cf8b
related_topics:
  - title: English version
    url: /en/linux/nmtui.html
    icon: bi bi-globe
---
# nmtui

Interfaccia utente solo testo per NetworkManager.
Usa le frecce e invio per navigare.
Maggiori informazioni: <https://networkmanager.dev/docs/api/latest/nmtui.html>.

- Apri interfaccia utente:

`nmtui`

- Mostra le reti disponibili, con opzioni per attivare o disattivare:

`nmtui connect`

- Per la connessione a una rete:

`nmtui connect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome|uuid|device|SSID</span>

- Cambia/Agiunge/Elimina una rete:

`nmtui edit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome|id</span>

- Imposta un hostname nuovo:

`nmtui hostname`
