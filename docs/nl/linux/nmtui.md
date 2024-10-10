---
layout: page
title: linux/nmtui (Nederlands)
description: "Tekstgebruikersinterface voor controle over NetworkManager."
content_hash: 22bb349e35ceacb9071a82e631078408416851b9
last_modified_at: 2024-10-10
related_topics:
  - title: English version
    url: /en/linux/nmtui.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/nmtui.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/nmtui.html
    icon: bi bi-globe
tldri18n_status: 2
---
# nmtui

Tekstgebruikersinterface voor controle over NetworkManager.
Gebruik pijltoetsen om te navigeren en gebruik Enter om een optie te selecteren.
Meer informatie: <https://networkmanager.pages.freedesktop.org/NetworkManager/NetworkManager/nmtui.html>.

- Open de gebruikersinterface:

`nmtui`

- Toon een lijst met alle beschikbare verbindingen, met de optie om deze te activeren danwel te deactiveren:

`nmtui connect`

- Verbind met een gegeven netwerk:

`nmtui connect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">naam|uuid|apparaat|SSID</span>

- Pas aan/Voeg toe/Verwijder een gegeven netwerk:

`nmtui edit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">naam|id</span>

- Stel de systeemhostnaam in:

`nmtui hostname`
