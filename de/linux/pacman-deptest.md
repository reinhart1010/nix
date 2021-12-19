---
layout: page
title: linux/pacman-deptest (Deutsch)
description: "Überprüfe alle angegebenen Abhängigkeiten und gib eine Liste von Abhängigkeiten zurück, welche auf dem System nicht erfüllt sind."
content_hash: 90c2871b592c0719da7df99af3a0b7e4e5a974df
related_topics:
  - title: English version
    url: /en/linux/pacman-deptest.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/pacman-deptest.html
    icon: bi bi-globe
---
# pacman --deptest

Überprüfe alle angegebenen Abhängigkeiten und gib eine Liste von Abhängigkeiten zurück, welche auf dem System nicht erfüllt sind.
Weitere Informationen: <https://man.archlinux.org/man/pacman.8>.

- Zeige Paketnamen von Abhängigkeiten an, welche nicht installiert sind:

`pacman --deptest `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paketname1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paketname2</span>

- Überprüfe ob ein installiertes Paket eine Minimalversion erfüllt:

`pacman --deptest "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bash>=5</span>`"`

- Überprüfe ob eine neuere version eines Paketes installiert ist:

`pacman --deptest "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bash>5</span>`"`

- Zeige Hilfe an:

`pacman --deptest --help`
