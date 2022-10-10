---
layout: page
title: linux/nordvpn (Deutsch)
description: "Kommandozeilen-Schnittstelle für NordVPN."
content_hash: c370f9983af7df34854c8dd1036cdb4d774f5c3c
related_topics:
  - title: English version
    url: /en/linux/nordvpn.html
    icon: bi bi-globe
---
# nordvpn

Kommandozeilen-Schnittstelle für NordVPN.
Weitere Informationen: <https://nordvpn.com/download/linux/>.

- Interaktiv bei einem NordVPN-Konto anmelden:

`nordvpn login`

- Zeige den Verbindungsstatus an:

`nordvpn status`

- Stelle eine Verbindung zum nächsten NordVPN-Server her:

`nordvpn connect`

- Liste alle verfügbaren Länder auf:

`nordvpn countries`

- Stelle eine Verbindung zu einem NordVPN-Server in einem bestimmten Land her:

`nordvpn connect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Germany</span>

- Stelle eine Verbindung zu einem NordVPN-Server in einem bestimmten Land und einer bestimmten Stadt her:

`nordvpn connect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Germany</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Berlin</span>

- Aktiviere die `autoconnect`-Option:

`nordvpn set autoconnect on`
