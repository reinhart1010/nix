---
layout: page
title: linux/pw-config (español)
description: "Enumera las rutas y secciones de configuración que utilizarán el servidor y los clientes de PipeWire."
content_hash: 0ec8af4c21a204f057cffd2d1ad21223e974e7a3
last_modified_at: 2024-09-27
related_topics:
  - title: English version
    url: /en/linux/pw-config.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/pw-config.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pw-config

Enumera las rutas y secciones de configuración que utilizarán el servidor y los clientes de PipeWire.
Más información: <https://docs.pipewire.org/page_man_pw-config_1.html>.

- Lista todos los archivos de configuración que se utilizarán:

`pw-config`

- Lista todos los archivos de configuración que utilizará el servidor PulseAudio de PipeWire:

`pw-config --name pipewire-pulse.conf`

- Lista todas las secciones de configuración utilizadas por el servidor PulseAudio de PipeWire:

`pw-config --name pipewire-pulse.conf list`

- Lista los fragmentos `context.properties` utilizados por los clientes JACK:

`pw-config --name jack.conf list context.properties`

- Lista las `context.properties` fusionadas utilizadas por los clientes JACK:

`pw-config --name jack.conf merge context.properties`

- Lista los `context.modules` fusionados utilizados por el servidor PipeWire y [r]eformat:

`pw-config --name pipewire.conf --recurse merge context.modules`

- Muestra la ayuda:

`pw-config --help`
