---
layout: page
title: linux/aplay (Deutsch)
description: "Command-line Musik Player für den ALSA-Soundkarten-Treiber."
content_hash: f4302531389f99acf0011fc415978d48cab0039c
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/linux/aplay.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/aplay.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/aplay.html
    icon: bi bi-globe
tldri18n_status: 2
---
# aplay

Command-line Musik Player für den ALSA-Soundkarten-Treiber.
Weitere Informationen: <https://manned.org/aplay>.

- Spiele eine bestimmte Datei (Abtastrate, Bittiefe, etc. werden automatisch für das Dateiformat erkannt):

`aplay `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei</span>

- Spiele die ersten 10 Sekunden einer bestimmten Datei mit 2500 Hz:

`aplay --duration=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>` --rate=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2500</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei</span>

- Spiele die rohe Datei mit 22050 Hz, mono, 8-bit, als Mu-Lw `.au` Datei:

`aplay --channels=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>` --file-type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">raw</span>` --rate=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">22050</span>` --format=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mu_law</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei</span>
