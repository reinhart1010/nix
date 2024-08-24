---
layout: page
title: linux/cu (español)
description: "Llama a otro sistema y actúa como terminal de marcado/serie o realiza transferencias de archivos sin comprobación de errores."
content_hash: ba037b72b969d769792c876a12503cba3569462e
last_modified_at: 2024-08-24
related_topics:
  - title: English version
    url: /en/linux/cu.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/cu.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># cu

Llama a otro sistema y actúa como terminal de marcado/serie o realiza transferencias de archivos sin comprobación de errores.
Más información: <https://manned.org/cu>.

- Abre un puerto serie determinado:

`sudo cu --line `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/ttyUSB0</span>

- Abre un puerto serie determinado con una velocidad en baudios determinada:

`sudo cu --line `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/ttyUSB0</span>` --speed `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">115200</span>

- Abre un puerto serie determinado con una velocidad en baudios determinada y emite un eco de caracteres localmente (modo semidúplex):

`sudo cu --line `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/ttyUSB0</span>` --speed `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">115200</span>` --halfduplex`

- Abre un puerto serie determinado con una velocidad en baudios, paridad y sin control de flujo por hardware o software:

`sudo cu --line `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/ttyUSB0</span>` --speed `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">115200</span>` --parity=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">par|odd|none</span>` --nortscts --nostop`

- Sale de la sesión `cu` cuando está conectado:

`~.`
