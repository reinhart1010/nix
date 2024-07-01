---
layout: page
title: osx/mist (español)
description: "MIST - macOS Installer Super Tool."
content_hash: e9871525797eda208ab21869f583fee06c9aa3ce
last_modified_at: 2024-07-01
related_topics:
  - title: English version
    url: /en/osx/mist.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/osx/mist.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># mist

MIST - macOS Installer Super Tool.
Descarga automáticamente Firmwares/Instaladores de macOS.
Más información: <https://github.com/ninxsoft/mist-cli>.

- Lista todos los firmwares de macOS disponibles para los Mac Silicon de Apple:

`mist list firmware`

- Lista todos los instaladores de macOS disponibles para Mac Intel, incluidos los instaladores universales para macOS Big Sur y versiones posteriores:

`mist list installer`

- Lista todos los instaladores de macOS compatibles con esta Mac, incluidos los instaladores universales de macOS Big Sur y posteriores:

`mist list installer --compatible`

- Lista todos los instaladores de macOS disponibles para Mac Intel, incluidas las betas tanto como también los instaladores universales para macOS Big Sur y versiones posteriores:

`mist list installer --include-betas`

- Lista solo el último instalador de macOS Sonoma para las Macs Intel, incluidos los instaladores universales de macOS Big Sur y posteriores:

`mist list installer --latest "macOS Sonoma"`

- Lista y exporta instaladores de macOS a un archivo CSV:

`mist list installer --export "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/ruta/a/archivo_con_datos_exportados.csv</span>`"`

- Descarga el último firmware de macOS Sonoma para los Mac Silicon de Apple, con un nombre personalizado:

`mist download firmware "macOS Sonoma" --firmware-name "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Install %NAME% %VERSION%-%BUILD%.ipsw</span>`"`

- Descarga una versión específica del instalador de macOS para Mac Intel, incluidos los instaladores universales de macOS Big Sur y posteriores:

`mist download installer "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">13.5.2</span>`" application`
