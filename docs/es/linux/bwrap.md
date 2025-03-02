---
layout: page
title: linux/bwrap (español)
description: "Ejecuta programas en un sandbox ligero."
content_hash: 590ba0ec9e139a876837ca27d46d495474e83431
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/linux/bwrap.html
    icon: bi bi-globe
tldri18n_status: 2
---
# bwrap

Ejecuta programas en un sandbox ligero.
Más información: <https://manned.org/bwrap>.

- Ejecuta un programa en un entorno de sólo lectura:

`bwrap --ro-bind / / `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/bin/bash</span>

- Da al entorno acceso a dispositivos, información de procesos y crea un `tmpfs` para el mismo:

`bwrap --dev-bind /dev /dev --proc /proc --ro-bind / / --tmpfs /tmp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/bin/bash</span>
