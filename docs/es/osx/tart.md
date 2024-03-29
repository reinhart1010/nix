---
layout: page
title: osx/tart (español)
description: "Crea, ejecuta y gestiona máquinas virtuales (VM) macOS y Linux en Apple Silicon."
content_hash: d3160a5621e3bcf7df2577bd27926caf6cc01113
last_modified_at: 2024-01-07
related_topics:
  - title: English version
    url: /en/osx/tart.html
    icon: bi bi-globe
tldri18n_status: 2
---
# tart

Crea, ejecuta y gestiona máquinas virtuales (VM) macOS y Linux en Apple Silicon.
Más información: <https://github.com/cirruslabs/tart>.

- Extrae una imagen de VM remota:

`tart pull `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">acme.io/org/nombre:tag</span>

- Clona una VM desde una fuente de imagen local o remota:

`tart clone `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">source-vm</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre-vm</span>

- Crea una nueva Mac VM a partir de un archivo ipsw específico:

`tart create --from-ipsw=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ultima|ruta/al/archivo.ipsw</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre-de-la-vm</span>

- Ejecuta una máquina virtual existente:

`tart run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre-de-la-vm</span>

- Ejecuta una máquina virtual existente con un directorio específico montado:

`tart run --dir=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/directorio</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/directorio local</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre-de-la-vm</span>

- Lista máquinas virtuales:

`tart list`

- Obtén la dirección IP de una máquina virtual en ejecución:

`tart ip `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre-de-la-vm</span>

- Cambia la resolución de pantalla de una máquina virtual:

`tart set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre-de-la-vm</span>` --display `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">640</span>`x`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">400</span>
