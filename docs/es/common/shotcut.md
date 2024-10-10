---
layout: page
title: common/shotcut (español)
description: "Un programa para la edición de vídeo."
content_hash: 89431604005d756497fa0b350073fe9ce783c749
last_modified_at: 2024-10-10
related_topics:
  - title: English version
    url: /en/common/shotcut.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/shotcut.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># shotcut

Un programa para la edición de vídeo.
Más información: <https://shotcut.org/notes/command-line-options/>.

- Inicia Shotcut:

`shotcut`

- Abre archivos de audio/vídeo:

`shotcut `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo1 ruta/al/archivo2 ...</span>

- Inicia con un controlador de audio específico:

`shotcut --SDL_AUDIODRIVER "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pulseaudio</span>`"`

- Inicia en pantalla completa:

`shotcut --fullscreen`

- Inicia con procesamiento GPU:

`shotcut --gpu`
