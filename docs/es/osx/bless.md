---
layout: page
title: osx/bless (español)
description: "Establece la capacidad de arranque del volumen y las opciones del disco de arranque."
content_hash: 0314f2820ba484db537db8d39d25e0b408b591f8
last_modified_at: 2024-02-15
related_topics:
  - title: English version
    url: /en/osx/bless.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/osx/bless.html
    icon: bi bi-globe
tldri18n_status: 2
---
# bless

Establece la capacidad de arranque del volumen y las opciones del disco de arranque.
Más información: <https://keith.github.io/xcode-man-pages/bless.8.html>.

- Bendice un volumen sólo con Mac OS X o Darwin, y crea los archivos BootX y `boot.efi` según sea necesario:

`bless --folder `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/Volumes/Mac OS X/System/Library/CoreServices</span>` --bootinfo --bootefi`

- Configura un volumen que contenga Mac OS 9 y Mac OS X para que sea el volumen activo:

`bless --mount `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Volumes/Mac OS</span>` --setBoot`

- Configura el sistema como NetBoot y localiza un servidor disponible:

`bless --netboot --server `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bsdp://255.255.255.255</span>

- Recopila información sobre el volumen seleccionado actualmente (según lo determinado por el firmware), adecuado para la canalización a un programa capaz de analizar las listas de propiedades:

`bless --info --plist`
