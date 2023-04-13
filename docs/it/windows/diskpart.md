---
layout: page
title: windows/diskpart (italiano)
description: "Gestore di dischi, volumi e partizioni."
content_hash: 3bfe99c203c95d24c556fc08aa73894d2a35966e
last_modified_at: 2023-04-13
related_topics:
  - title: English version
    url: /en/windows/diskpart.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/windows/diskpart.html
    icon: bi bi-globe
---
# diskpart

Gestore di dischi, volumi e partizioni.
Maggiori informazioni: <https://learn.microsoft.com/windows-server/administration/windows-commands/diskpart>.

- Esegui diskpart da solo in un prompt dei comandi da amministratore per inserire la sua riga di comando:

`diskpart`

- Elenca tutti i dischi:

`list disk`

- Seleziona un volume:

`select volume `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">volume</span>

- Assegna una lettera di unità al volume selezionato:

`assign letter `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">lettera</span>

- Crea una nuova partizione:

`create partition primary`

- Attiva il volume selezionato:

`active`

- Esci da diskpart:

`exit`
