---
layout: page
title: linux/arecord (Deutsch)
description: "Sound Recorder für den ALSA-Soundkarten-Treiber."
content_hash: efe2b411dd0a93e0662fe86c83c8ed1e4d19649e
related_topics:
  - title: English version
    url: /en/linux/arecord.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/arecord.html
    icon: bi bi-globe
---
# arecord

Sound Recorder für den ALSA-Soundkarten-Treiber.
Weitere Informationen: <https://manned.org/arecord>.

- Nehme einen Schnipsel in CD-Qualität auf (beende die Aufnahme mit CTRL-C):

`arecord -vv --format=cd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zur/datei.wav</span>

- Nehme einen Schnipsel in CD-Qualität auf mit einer festen Länge von 10 Sekunden:

`arecord -vv --format=cd --duration=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zur/datei.wav</span>

- Nehme einen Schnipsel auf und speichere es als MP3 (beende die Aufnahme mit CTRL-C):

`arecord -vv --format=cd --file-type raw | lame -r - `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.mp3</span>

- Liste alle Soundkarten und digitalen Ausgabe Geräte:

`arecord --list-devices`

- Benutze das interaktive Interface (z.B. Space oder Enter für Play oder Pause):

`arecord --interactive`
