---
layout: page
title: linux/arecord (Deutsch)
description: "Sound Recorder für den ALSA-Soundkarten-Treiber."
content_hash: 17acf09c085d9de11042d7e77e943f728737db1c
last_modified_at: 2024-10-07
related_topics:
  - title: English version
    url: /en/linux/arecord.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/arecord.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># arecord

Sound Recorder für den ALSA-Soundkarten-Treiber.
Weitere Informationen: <https://manned.org/arecord>.

- Nehme einen Schnipsel in CD-Qualität auf (beende die Aufnahme mit CTRL-C):

`arecord -vv --format=cd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei.wav</span>

- Nehme einen Schnipsel in CD-Qualität auf mit einer festen Länge von 10 Sekunden:

`arecord -vv --format=cd --duration=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei.wav</span>

- Nehme einen Schnipsel auf und speichere es als MP3 (beende die Aufnahme mit CTRL-C):

`arecord -vv --format=cd --file-type raw | lame -r - `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei.mp3</span>

- Liste alle Soundkarten und digitalen Ausgabe Geräte:

`arecord --list-devices`

- Benutze das interaktive Interface (z.B. Space oder Enter für Play oder Pause):

`arecord --interactive`
