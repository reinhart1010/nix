---
layout: page
title: common/musescore (Deutsch)
description: "MuseScore 3 Notenblatt-Editor."
content_hash: b776cdcf20ca88b2f9eee3bb480a2cbe7f09df7e
related_topics:
  - title: English version
    url: /en/common/musescore.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/musescore.html
    icon: bi bi-globe
---
# musescore

MuseScore 3 Notenblatt-Editor.
Weitere Informationen: <https://musescore.org/en/handbook/3/command-line-options>.

- Verwende einen bestimmten Audio-Treiber:

`musescore --audio-driver `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jack|alsa|portaudio|pulse</span>

- Setze die MP3 Output-Bitrate in kbit/s:

`musescore --bitrate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bitrate</span>

- Starte MuseScore im Debug-Modus:

`musescore --debug`

- Aktiviere experimentelle Funktionen, wie Layer:

`musescore --experimental`

- Exportiere eine Datei in ein anderes Format. Dieses hängt von der Dateierweiterung ab:

`musescore --export-to `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">output_datei</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input_datei</span>

- Zeige Unterschiede zwischen zwei Partituren:

`musescore --diff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei2</span>

- Gib eine MIDI-Importoperationsdatei an:

`musescore --midi-operations `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei</span>
