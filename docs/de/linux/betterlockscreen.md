---
layout: page
title: linux/betterlockscreen (Deutsch)
description: "Einfacher, minimalistischer Sperrbildschirm."
content_hash: ccb17fff9e18d98c6ba57ae11c4382c7eb420757
last_modified_at: 2024-10-25
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
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/betterlockscreen.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># betterlockscreen

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
