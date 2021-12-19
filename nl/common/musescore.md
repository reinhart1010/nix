---
layout: page
title: common/musescore (Nederlands)
description: "MuseScore 3 bladmuziek bewerker."
content_hash: 05c93d1a40f8947bf4fe8a3a0acc84f52b45266c
related_topics:
  - title: Deutsch version
    url: /de/common/musescore.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/musescore.html
    icon: bi bi-globe
---
# musescore

MuseScore 3 bladmuziek bewerker.
Meer informatie: <https://musescore.org/en/handbook/3/command-line-options>.

- Gebruik een specifiek audio stuurprogramma:

`musescore --audio-driver `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jack|alsa|portaudio|pulse</span>

- Stel de MP3 uitvoer bitsnelheid in in kbit/s:

`musescore --bitrate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bitsnelheid</span>

- Open MuseScore in debug modus:

`musescore --debug`

- Schakel experimentele funcies in, bijvoorbeeld lagen:

`musescore --experimental`

- Exporteer het gegeven bestand naar het gegeven uitvoer bestand. Het bestandstype hangt af van de gegeven extentie:

`musescore --export-to `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">uitvoer_bestand</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">invoer_bestand</span>

- Geef het verschil tussen de gegeven partituren:

`musescore --diff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand2</span>

- Specificeer een MIDI invoer operaties bestand:

`musescore --midi-operations `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>
