---
layout: page
title: linux/debsecan (español)
description: "Analizador de seguridad de Debian, es una herramienta para enumerar vulnerabilidades en una instalación Debian en particular."
content_hash: 35193d45cdd9e94aea69c4a4b418a2ad27c0638c
last_modified_at: 2024-12-21
related_topics:
  - title: English version
    url: /en/linux/debsecan.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/debsecan.html
    icon: bi bi-globe
tldri18n_status: 2
---
# debsecan

Analizador de seguridad de Debian, es una herramienta para enumerar vulnerabilidades en una instalación Debian en particular.
Más información: <https://gitlab.com/fweimer/debsecan>.

- Lista de paquetes instalados vulnerables en el host actual:

`debsecan`

- Lista de paquetes instalados vulnerables de una versión específica:

`debsecan --suite `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_la_versión</span>

- Lista solo vulnerabilidades arregladas:

`debsecan --suite `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_la_versión</span>` --only-fixed`

- Lista solo vulnerabilidades arregladas de inestable ("sid") y envía un correo a root:

`debsecan --suite `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sid</span>` --only-fixed --format `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">report</span>` --mailto `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">root</span>` --update-history`

- Actualiza paquetes vulnerables instalados:

`sudo apt upgrade $(debsecan --only-fixed --format `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquetes</span>`)`
