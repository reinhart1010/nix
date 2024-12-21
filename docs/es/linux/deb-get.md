---
layout: page
title: linux/deb-get (español)
description: "Funcionalidad `apt-get` para paquetes `.deb` publicados en repositorios de terceros o a través de descarga directa."
content_hash: 5775634437498a93e1aec4bf5372502f6dfde61e
last_modified_at: 2024-12-21
related_topics:
  - title: English version
    url: /en/linux/deb-get.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/deb-get.html
    icon: bi bi-globe
tldri18n_status: 2
---
# deb-get

Funcionalidad `apt-get` para paquetes `.deb` publicados en repositorios de terceros o a través de descarga directa.
Funciona con distribuciones Linux que usan `apt-get`.
Más información: <https://github.com/wimpysworld/deb-get>.

- Actualiza la lista de paquetes y versiones disponibles:

`deb-get update`

- Busca un paquete dado:

`deb-get search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquete</span>

- Muestra información sobre un paquete:

`deb-get show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquete</span>

- Instala un paquete o lo actualiza a la última versión disponible:

`deb-get install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquete</span>

- Elimina un paquete (utilizando `purge` en su lugar, también elimina sus archivos de configuración):

`deb-get remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquete</span>

- Actualiza todos los paquetes instalados a sus versiones más recientes disponibles:

`deb-get upgrade`

- Lista todos los paquetes disponibles:

`deb-get list`
