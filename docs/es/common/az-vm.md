---
layout: page
title: common/az-vm (español)
description: "Administra máquinas virtuales en Azure."
content_hash: 2dcd19cc76fc605ffd47848a37a2923605de9d36
last_modified_at: 2024-03-14
related_topics:
  - title: English version
    url: /en/common/az-vm.html
    icon: bi bi-globe
tldri18n_status: 2
---
# az vm

Administra máquinas virtuales en Azure.
Parte de `azure-cli` (también conocido como `az`).
Más información: <https://learn.microsoft.com/cli/azure/vm>.

- Lista los detalles de las máquinas virtuales disponibles:

`az vm list`

- Crea una máquina virtual usando la imagen por defecto de Ubuntu y genera claves SSH:

`az vm create --resource-group `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">grupo_de_recursos</span>` --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre</span>` --image `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">UbuntuLTS</span>` --admin-user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">usuario_azure</span>` --generate-ssh-keys`

- Detiene una máquina virtual:

`az vm stop --resource-group `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">grupo_de_recursos</span>` --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre</span>

- Desasigna una máquina virtual:

`az vm deallocate --resource-group `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">grupo_de_recursos</span>` --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre</span>

- Inicia una máquina virtual:

`az vm start --resource-group `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">grupo_de_recursos</span>` --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre</span>

- Reinicia una máquina virtual:

`az vm restart --resource-group `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">grupo_de_recursos</span>` --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre</span>

- Lista las imágenes de VM disponibles en el Azure Marketplace:

`az vm image list`
