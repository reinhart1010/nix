---
layout: page
title: common/ansiweather (Deutsch)
description: "Ein Shell-Skript um die aktuellen Wetterbedingungen in einem Terminal anzuzeigen."
content_hash: 502c261bce4c55a8512e69410a3512f743e285b0
last_modified_at: 2022-12-19
related_topics:
  - title: English version
    url: /en/common/ansiweather.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/ansiweather.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/ansiweather.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/ansiweather.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/ansiweather.html
    icon: bi bi-globe
---
# ansiweather

Ein Shell-Skript um die aktuellen Wetterbedingungen in einem Terminal anzuzeigen.
Weitere Informationen: <https://github.com/fcambus/ansiweather>.

- Zeige eine Vorhersage für die nächsten fünf Tage für Rzeszow, Polen in metrischen Einheiten an:

`ansiweather -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">metric</span>` -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>` -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Rzeszow,PL</span>

- Zeige eine Vorhersage mit Symbolen und Tageslichtdaten für den aktuellen Standort an:

`ansiweather -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">true</span>` -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">true</span>

- Zeige eine Vorhersage mit Wind- und Luftfeuchtigkeitsdaten für den aktuellen Standort an:

`ansiweather -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">true</span>` -h `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">true</span>
