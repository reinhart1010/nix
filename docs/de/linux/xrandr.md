---
layout: page
title: linux/xrandr (Deutsch)
description: "Setzt die Auflösung, Orientierung und/oder Reflektion eines Bildschirmausgangs."
content_hash: eebcce4fd088e99a5db30f253a85b5f89f6e31c4
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/linux/xrandr.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/xrandr.html
    icon: bi bi-globe
tldri18n_status: 2
---
# xrandr

Setzt die Auflösung, Orientierung und/oder Reflektion eines Bildschirmausgangs.
Weitere Informationen: <https://www.x.org/releases/current/doc/man/man1/xrandr.1.xhtml>.

- Zeige den momentanen Systemzustand an (erkannte Bildschirme, Auflösungen, ...):

`xrandr --query`

- Deaktiviere nicht mehr verbundene Ausgangsgeräte und aktiviere verbundene Ausgänge mit Standardeinstellungen:

`xrandr --auto`

- Ändere die Auflösung und Bildfrequenz von DisplayPort 1 zu 1920x1080, 60Hz:

`xrandr --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">DP1</span>` --mode `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1920x1080</span>` --rate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">60</span>

- Setze die Auflösung von HDMI auf 1280x1024 und platziere HDMI1 rechts von DP1:

`xrandr --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">HDMI2</span>` --mode `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1280x1024</span>` --right-of `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">DP1</span>

- Deaktiviere den Ausgang von VGA1:

`xrandr --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">VGA1</span>` --off`

- Setze die Bildschirmhelligkeit von LVDS1 auf 50%:

`xrandr --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">LVDS1</span>` --brightness `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0.5</span>
