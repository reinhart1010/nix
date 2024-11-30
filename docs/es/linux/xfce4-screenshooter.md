---
layout: page
title: linux/xfce4-screenshooter (español)
description: "La herramienta de captura de pantalla de XFCE4."
content_hash: 85eba60d66cf857f0ce90f7dad7003de613596c0
last_modified_at: 2024-11-30
related_topics:
  - title: English version
    url: /en/linux/xfce4-screenshooter.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/xfce4-screenshooter.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/xfce4-screenshooter.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/xfce4-screenshooter.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># xfce4-screenshooter

La herramienta de captura de pantalla de XFCE4.
Más información: <https://docs.xfce.org/apps/xfce4-screenshooter/start>.

- Inicia la interfaz gráfica de usuario (GUI) de captura de pantalla:

`xfce4-screenshooter`

- Toma una captura de pantalla de toda la pantalla y lanza la GUI para preguntar cómo proceder:

`xfce4-screenshooter --fullscreen`

- Toma una captura de pantalla de toda la pantalla y la guarda en el directorio especificado:

`xfce4-screenshooter --fullscreen --save `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/directorio</span>

- Espera un tiempo antes de tomar la captura de pantalla:

`xfce4-screenshooter --delay `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">segundos</span>

- Toma una captura de pantalla de una región de la pantalla (selecciona usando el ratón):

`xfce4-screenshooter --region`

- Toma una captura de pantalla de la ventana activa, y la copia al portapapeles:

`xfce4-screenshooter --window --clipboard`

- Toma una captura de pantalla de la ventana activa, y la abre con un programa elegido:

`xfce4-screenshooter --window --open `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gimp</span>
