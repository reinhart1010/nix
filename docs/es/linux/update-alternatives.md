---
layout: page
title: linux/update-alternatives (español)
description: "Mantiene convenientemente enlaces simbólicos para determinar los comandos predeterminados."
content_hash: d91188987cba544a2f66282aca37346dcb7ddff1
last_modified_at: 2024-11-05
related_topics:
  - title: English version
    url: /en/linux/update-alternatives.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/update-alternatives.html
    icon: bi bi-globe
tldri18n_status: 2
---
# update-alternatives

Mantiene convenientemente enlaces simbólicos para determinar los comandos predeterminados.
Más información: <https://manned.org/update-alternatives>.

- Agrega un enlace simbólico:

`sudo update-alternatives --install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/enlace_simbólico</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/comando</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">prioridad</span>

- Configura un enlace simbólico para 'java':

`sudo update-alternatives --config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">java</span>

- Quita un enlace simbólico:

`sudo update-alternatives --remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">java</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/opt/java/jdk1.8.0_102/bin/java</span>

- Muestra información sobre un comando específico:

`update-alternatives --display `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">java</span>

- Muestra todos los comandos y su selección actual:

`update-alternatives --get-selections`
