---
layout: page
title: linux/betterlockscreen (Deutsch)
description: "Einfacher, minimalistischer Sperrbildschirm."
content_hash: ccb17fff9e18d98c6ba57ae11c4382c7eb420757
last_modified_at: 2024-10-26
related_topics:
  - title: English version
    url: /en/linux/betterlockscreen.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/betterlockscreen.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/betterlockscreen.html
    icon: bi bi-globe
tldri18n_status: 2
---
# betterlockscreen

Einfacher, minimalistischer Sperrbildschirm.
Weitere Informationen: <https://github.com/betterlockscreen/betterlockscreen>.

- Sperre den Bildschirm:

`betterlockscreen --lock`

- Ändere den Hintergrund des Sperrbildschirms:

`betterlockscreen -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/bild.png</span>

- Sperre den Bildschirm und zeige benutzerdefinierten Text an:

`betterlockscreen -l pixel -t "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">benutzerdefinierter Sperrbildschirmtext</span>`"`

- Sperre den Bildschirm mit einer benutzerdefinierten Monitor-Auszeit in Sekunden:

`betterlockscreen --off `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>` -l`
