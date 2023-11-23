---
layout: page
title: osx/mktemp (español)
description: "Crea un archivo o directorio temporal."
content_hash: 30ca868cc98aaf7666c8b7147c0cc833eecb7415
last_modified_at: 2023-11-23
related_topics:
  - title: English version
    url: /en/osx/mktemp.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/osx/mktemp.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># mktemp

Crea un archivo o directorio temporal.
Más información: <https://keith.github.io/xcode-man-pages/mktemp.1.html>.

- Crea un archivo temporal vacío e imprime su ruta absoluta:

`mktemp`

- Usa un directorio personalizado (por defecto la salida de `getconf DARWIN_USER_TEMP_DIR`, o `/tmp`):

`mktemp --tmpdir=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/ruta/a/tempdir</span>

- Usa una plantilla de ruta personalizada (las `X` se sustituyen por caracteres alfanuméricos aleatorios):

`mktemp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/tmp/ejemplo.XXXXXXXX</span>

- Usa un prefijo de nombre de archivo personalizado:

`mktemp -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ejemplo</span>

- Crea un directorio temporal vacío e imprime su ruta absoluta:

`mktemp --directory`
