---
layout: page
title: common/mpremote (español)
description: "Controla remotamente dispositivos MicroPython."
content_hash: 3618ac1644188e956f899c8bd984fb8c3e07c555
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/mpremote.html
    icon: bi bi-globe
tldri18n_status: 2
---
# mpremote

Controla remotamente dispositivos MicroPython.
Más información: <https://docs.micropython.org/en/latest/reference/mpremote.html>.

- Lista todos los dispositivos MicroPython conectados:

`mpremote connect list`

- Abre una sesión REPL interactiva con un dispositivo conectado:

`mpremote connect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dispositivo</span>

- Ejecuta un script local en un dispositivo conectado:

`mpremote run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/script.py</span>

- Monta un directorio local en el dispositivo:

`mpremote mount `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/directorio</span>

- Instala un paquete mip en el dispositivo:

`mpremote mip install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquete</span>
