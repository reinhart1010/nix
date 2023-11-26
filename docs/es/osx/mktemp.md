---
layout: page
title: osx/mktemp (español)
description: "Crea un archivo o directorio temporal."
content_hash: 30ca868cc98aaf7666c8b7147c0cc833eecb7415
last_modified_at: 2023-11-26
related_topics:
  - title: English version
    url: /en/osx/mktemp.html
    icon: bi bi-globe
tldri18n_status: 2
---
# mktemp

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
