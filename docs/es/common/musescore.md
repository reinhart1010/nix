---
layout: page
title: common/musescore (español)
description: "MuseScore editor de música de 3 hojas."
content_hash: fb9da8e2858340b23f3bca6e994b5449f512dbcb
last_modified_at: 2024-11-24
related_topics:
  - title: Deutsch version
    url: /de/common/musescore.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/musescore.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/musescore.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/musescore.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/musescore.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># musescore

MuseScore editor de música de 3 hojas.
Vea también: `lilypond`.
Más información: <https://musescore.org/en/handbook/3/command-line-options>.

- Utiliza un controlador de audio específico:

`musescore --audio-driver `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jack|alsa|portaudio|pulse</span>

- Establece el bitrate de salida MP3 en kbit/s:

`musescore --bitrate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bitrate</span>

- Inicia MuseScore en modo depuración:

`musescore --debug`

- Permite características experimentales, como capas:

`musescore --experimental`

- Exporta el archivo dado al archivo de salida especificado. El tipo de archivo depende de la extensión dada:

`musescore --export-to `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archivo_de_salida</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archivo_de_entrada</span>

- Imprime las diferencias entre las puntuaciones (scores) dadas:

`musescore --diff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo2</span>

- Especifica un archivo de operaciones de importación MIDI:

`musescore --midi-operations `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>
