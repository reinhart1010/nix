---
layout: page
title: common/az-sshkey (español)
description: "Administra claves públicas SSH con máquinas virtuales."
content_hash: 7af0b6f765335c35719f393cb1c0a1c3812a7f6f
last_modified_at: 2023-10-15
related_topics:
  - title: English version
    url: /en/common/az-sshkey.html
    icon: bi bi-globe
---
# az sshkey

Administra claves públicas SSH con máquinas virtuales.
Parte de `azure-cli` (también conocido como `az`).
Más información: <https://learn.microsoft.com/cli/azure/sshkey>.

- Crea una nueva clave SSH:

`az sshkey create --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre</span>` --resource-group `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">grupo_de_recursos</span>

- Sube una clave SSH existente:

`az sshkey create --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre</span>` --resource-group `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">grupo_de_recursos</span>` --public-key "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">@ruta/de/llave.pub</span>`"`

- Lista todas las claves públicas SSH:

`az sshkey list`

- Muestra información sobre una clave pública SSH:

`az sshkey show --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre</span>` --resource-group `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">grupo_de_recursos</span>
