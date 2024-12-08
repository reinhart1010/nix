---
layout: page
title: linux/wf-recorder (español)
description: "Screencast para Wayland opcionalmente con audio."
content_hash: 6eebdeddf858d988ddd2e7be37c84b03c0a86c1f
last_modified_at: 2024-12-08
related_topics:
  - title: English version
    url: /en/linux/wf-recorder.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/wf-recorder.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># wf-recorder

Screencast para Wayland opcionalmente con audio.
Por defecto necesita terminar el proceso con Ctrl-C.
Más información: <https://github.com/ammen99/wf-recorder>.

- Grabación de un archivo MP4:

`wf-recorder --file=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">salida.mp4</span>

- Graba video incluyendo audio; y esto incluye acceso al micrófono y los sonidos del sistema:

`wf-recorder --audio --file=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/ruta/al/archivo_con_audio.webm</span>

- Selecciona y graba una porción de la pantalla utilizando `slurp`, guardando en `recording.mp4` de forma predeterminada:

`wf-recorder -g "$(slurp)"`
