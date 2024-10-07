---
layout: page
title: common/az-vm (español)
description: "Gestiona máquinas virtuales en Azure."
content_hash: 611a4e319322068ab10c3c4fcfca86c2fb2d0a2f
last_modified_at: 2024-10-07
related_topics:
  - title: English version
    url: /en/common/az-vm.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/az-vm.html
    icon: bi bi-globe
tldri18n_status: 2
---
# az vm

Gestiona máquinas virtuales en Azure.
Parte de `azure-cli` (también conocido como `az`).
Más información: <https://learn.microsoft.com/cli/azure/vm>.

- Muestra una tabla de Máquinas Virtuales disponibles:

`az vm list --output table`

- Crea una máquina virtual usando la imagen por defecto de Ubuntu y genera las claves SSH:

`az vm create --resource-group `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rg</span>` --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_vm</span>` --image `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">UbuntuLTS</span>` --admin-user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">usuarioazure</span>` --generate-ssh-keys`

- Detiene una Máquina Virtual:

`az vm stop --resource-group `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rg</span>` --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_la_máquina_virtual</span>

- Desasigna una máquina virtual:

`az vm deallocate --resource-group `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rg</span>` --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_la_máquina virtual</span>

- Inicia una Máquina Virtual:

`az vm start --resource-group `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rg</span>` --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_la_máquina_virtual</span>

- Reinicia una Máquina Virtual:

`az vm restart --resource-group `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rg</span>` --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_de_la_máquina_virtual</span>

- Lista de imágenes de máquinas virtuales disponibles en Azure Marketplace:

`az vm image list`
