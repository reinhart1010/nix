---
layout: page
title: common/ansiweather (Deutsch)
description: "Ein Shell-Skript um die aktuellen Wetterbedingungen in einem Terminal anzuzeigen."
content_hash: 9360c793cb6b128ef4c54f4191e2b795d20db5a3
last_modified_at: 2024-10-13
related_topics:
  - title: English version
    url: /en/common/ansiweather.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/ansiweather.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/ansiweather.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/ansiweather.html
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
tldri18n_status: 2
---
# ansiweather

Ein Shell-Skript um die aktuellen Wetterbedingungen in einem Terminal anzuzeigen.
Weitere Informationen: <https://github.com/fcambus/ansiweather>.

- Zeige eine Vorhersage für die nächsten sieben Tage für Rzeszow, Polen in metrischen Einheiten an:

`ansiweather -u metric -f 7 -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Rzeszow,PL</span>

- Zeige eine Vorhersage mit Symbolen und Tageslichtdaten für den aktuellen Standort an:

`ansiweather -F -s true -d true`

- Zeige eine Vorhersage mit Wind- und Luftfeuchtigkeitsdaten für den aktuellen Standort an:

`ansiweather -w true -h true`
