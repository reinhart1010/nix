---
layout: page
title: linux/nordvpn (Deutsch)
description: "Kommandozeilen-Schnittstelle für NordVPN."
content_hash: 28238307ea5109373f8341476650b103b0d42488
related_topics:
  - title: English version
    url: /en/linux/nordvpn.html
    icon: bi bi-globe
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/nordvpn.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># nordvpn

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

- Stelle eine Verbinding zu einem NordVPN-Server in einem bestimmten Land und einer bestimmten Stadt her:

`nordvpn connect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Germany</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Berlin</span>

- Aktiviere die `autoconnect`-Option:

`nordvpn set autoconnect on`
